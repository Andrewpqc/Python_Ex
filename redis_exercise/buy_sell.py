"""
redis event
"""
import redis, time


def sell(conn, item_name, sellerID, price):
    """
    将商品放到市场上
    :param conn: redis 连接对象
    :param item_name: 商品名
    :param sellerID: 发布者ID
    :param price: 标价
    :return:
        True:success,
        False:fail,
        None:该商品不属于该发布者
    """
    sellerID = str(sellerID)
    price = int(price)
    inventory = "inventory:%s" % sellerID
    item = item_name + ":" + sellerID
    seller = "user:%s" % sellerID
    end = time.time() + 5
    pipe = conn.pipeline()
    while time.time() < end:
        try:
            pipe.watch(inventory)  # 监视用户包裹发生的变化，防止同时更改
            if not pipe.sismember(inventory, item_name):  # 所卖的商品不在该用户的包中
                pipe.unwatch()
                return None
            pipe.multi()
            pipe.zadd("market", item, price)  # 在市场上添加该商品
            pipe.srem(inventory, item_name)  # 移除用户包中的该商品
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            return False


def buy(conn, item_name_in_market, buyerID):
    """
    购买市场上的商品
    :param conn: redis连接对象
    :param item_name_in_market:需要购买的商品的名字(在市场上的名字)
    :param buyerID: 购买者ID
    :return:
        True:success,
        False:fail
    """
    sellerID = str(buyerID)
    inventory = "inventory:%s" % buyerID
    item_name, sellerID = item_name_in_market.split(":")
    seller = "user:%s" % sellerID
    buyer = "user:%s" % buyerID
    end = time.time() + 5
    price = int(float(str(conn.zscore("market",
                                      item_name_in_market))))  # 获得该商品的价格
    pipe = conn.pipeline()
    # 最长阻塞5秒
    while time.time() < end:
        try:
            pipe.watch(inventory)  # 监视用户包裹发生的变化，防止同时更改
            pipe.watch(seller)  # 简视卖方的个人信息,防止同时更改
            pipe.watch(buyer)
            pipe.watch("market")
            pipe.multi()
            pipe.zrem("market", item_name_in_market)  # 在市场上移除该商品
            pipe.sadd(inventory, item_name)  # 向购买者包中添加该商品
            # update fund
            pipe.hincrby(seller, "funds", price)
            pipe.hincrby(buyer, "funds", -price)
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            return False


if __name__ == '__main__':
    conn = redis.Redis()
    conn.hmset("user:1", {"name": "Frank", "funds": 20})
    conn.hmset("user:2", {"name": "Jack", "funds": 15})
    conn.hmset("user:3", {"name": "Jim", "funds": 12})
    print("create three users!")
    # 创建对应的用户本来拥有了商品
    conn.sadd("inventory:1", "A", "B", "C")
    conn.sadd("inventory:2", "D", "E", "F")
    conn.sadd("inventory:3", "G", "H", "I")
    print("create three inventorys for the three users!")
    print("before sale ,user 1's inventory:", conn.smembers("inventory:1"))
    sell(conn, "A", 1, 50)
    print("user 1 put A to market")
    print("after sale ,user 1's inventory:", conn.smembers("inventory:1"))
    print("current market:", conn.zrange("market", 0, -1, withscores=True))
    print("user1's funds:", conn.hget("user:1", "funds"))
    print("user2's funds:", conn.hget("user:2", "funds"))
    buy(conn, "A:1", 2)
    print("now user 2 buy A from market")
    print("current market:", conn.zrange("market", 0, -1, withscores=True))
    print("user1's funds:", conn.hget("user:1", "funds"))
    print("user2's funds:", conn.hget("user:2", "funds"))
    # 清理
    conn.delete("user:1", "user:2", "user:3", "inventory:1", "inventory:2",
                "inventory:3", "market")
