"""
redis事务与redis非事务型流水线的区别：
pipe=conn.pipeline()
这个函数在不传参数或者传一个True的时候，使用的是redis的事务，
它的命令会被一次性送至redis服务器，然后逐个执行。redis事务的
一个好处是，它的命令执行不会被其他的客户端所影响。同时，一次性
发送所有的命令可以减少客户端与服务器之间的通信次数，提高性能。

这个函数在传入False为参数是，使用的是redis的非事务型流水线，
它不会执行multi和exec从而相较于redis事务来说，可以进一步提
升性能。但它对用户向redis发送的多个命令有要求：一个命令的执行
结果不会影响另一个命令的输入


"""



def add_update_contact(conn, user, contact):
    """
    向列表中添加或者更新近期联系人
    :param conn: 连接对象
    :param user: 用户
    :param contact: 最近联系人
    :return: None
    """
    recent_contact_list = "recent:%s" % user
    pipe = conn.pipeline(True)  # 使用redis事务
    pipe.lrem(recent_contact_list, contact)  # 如果该用户已经存在则删除之
    pipe.lpush(recent_contact_list, contact)  # 添加该用户
    pipe.ltrim(recent_contact_list, 0, 2)  # 只保留最新的3个最近联系人
    pipe.execute()  # 执行上述命令

def delete_contact(conn,user,contact):
    """
    删除每一个联系人
    :param conn: 连接对象
    :param user: 用户
    :param contact: 待删除的联系人
    :return: None
    """
    recent_contact_list="recent:%s"%user
    conn.lrem(recent_contact_list,contact)


def fetch_autocomplete_list(conn,user,prefix):
    """
    获取指定用户，特定前缀的最近联系人列表
    :param conn: 连接对象
    :param user: 当前用户
    :param prefix: 联系人名前缀
    :return: 匹配的用户列表
    """
    recent_contact_list = "recent:%s" % user
    candidates=conn.lrange(recent_contact_list,0,-1)

    matches=[]
    for candidate in candidates:
        print(candidate, "dd")
        if candidate.decode().lower().startswith(prefix):
            matches.append(candidate)
    return matches

if __name__ == '__main__':
    from redis import Redis
    conn = Redis()
    add_update_contact(conn,"benjim","jjjj")
    add_update_contact(conn,"benjim","jjk")
    add_update_contact(conn,"benjim","jjllll")
    add_update_contact(conn,"benjim","kkk")
    add_update_contact(conn,"benjim","jk")
    add_update_contact(conn,"benjim","kjkllllk")
    add_update_contact(conn,"benjim","jjk")
    recent=fetch_autocomplete_list(conn,"benjim","j")
    for i in recent:
        print(i.decode())

    conn.delete("recent:benjim")


