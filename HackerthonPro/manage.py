import os
from app import create_app,db
from flask_script import Manager,Shell
from app.models import TrainDesData,Comment,Movie
from flask_migrate import Migrate,MigrateCommand
app=create_app("default")
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
    """自动加载环境"""
    return dict(app=app,db=db,TrainDesData=TrainDesData,
                Comment=Comment,Movie=Movie)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

@manager.command
def get_theta():
    import math
    theta = [0, 0, 0]
    step = 0.01
    comments = TrainDesData.query.all()
    for m in range(40000):
        xxx=0
        for comment in comments:
            print(xxx)
            xxx+=1
            x = [1, float(comment.poscount), float(comment.nagcount)]
            feature_sum = 0
            for i in range(3):
                feature_sum += theta[i]*x[i]

            h = 1 / (1+math.e**-(feature_sum))
            for i in range(3):
                theta[i] = theta[i] + step*(comment.emotion-h)*x[i]
    print("Theta Gotten: ", theta)
    return theta


# [44751.0773169849, 57001.01137011098, 6551.006424249747] 5000*500样本
# [89501.0773157487, 114001.01136854848, 13101.006424319943] 10000*500样本
# [179001.07731027488, 228001.01136506314, 26201.006424205938] 20000*500样本
# [358001.0773901941, 456001.0114158664, 52401.00642363201] 40000*500样本

@manager.command
def get_emotion():
    print("Calculating thetas...")
    import math
    #get_theta()计算出来的如下结果：
    theta=[358000.224245114, 456000.10811124597, 52400.042114550015]

    print("Done!")
    comments = Comment.query.all()
    for comment in comments:
        x = [1, float(comment.poscount), float(comment.nagcount)]
        hypothesis = 0.0
        feature_sum = 0
        for i in range(3):
            feature_sum += theta[i]*x[i]
        hypothesis = 1 / (1+math.e**-(feature_sum))
        print(hypothesis)
        if 0.0 < hypothesis < 0.25:
            comment.result = 1.0#A
            db.session.add(comment)
            db.session.commit()
        elif 0.25 <= hypothesis <0.6:
            comment.result = 2.0#AA
            db.session.add(comment)
            db.session.commit()
        elif 0.6 <= hypothesis < 0.85:
            comment.result = 3.0#AAA
            db.session.add(comment)
            db.session.commit()
        elif 0.85<=hypothesis<1.0:
            comment.result=4.0#AAAA
            db.session.add(comment)
            db.session.commit()

@manager.command
def fake():
    movies=Movie.query.all()
    movies[0].rate1=0.002*101
    movies[0].rate2=0.15256*101
    movies[0].rate3=0.25156*101
    movies[0].rate4=(1-0.002-0.15256-0.25156)*101
    db.session.add(movies[0])
    db.session.commit()

    movies[1].rate1 = 0.05 * 101
    movies[1].rate2 = 0.09 * 101
    movies[1].rate3 = 0.35 * 101
    movies[1].rate4 = (1 - 0.05 - 0.09 - 0.35) * 101
    db.session.add(movies[1])
    db.session.commit()

    movies[2].rate1 = 0.07 * 101
    movies[2].rate2 = 0.21 * 101
    movies[2].rate3 = 0.42 * 101
    movies[2].rate4 = (1 - 0.07 - 0.21 - 0.42) * 101
    db.session.add(movies[2])
    db.session.commit()

    movies[3].rate1 = 0.03 * 101
    movies[3].rate2 = 0.1956 * 101
    movies[3].rate3 = 0.3556 * 101
    movies[3].rate4 = (1 - 0.03 - 0.1956 - 0.3556) * 101
    db.session.add(movies[3])
    db.session.commit()

    movies[4].rate1 = 0.04 * 101
    movies[4].rate2 = 0.15256 * 101
    movies[4].rate3 = 0.25156 * 101
    movies[4].rate4 = (1 - 0.04 - 0.15256 - 0.25156) * 101
    db.session.add(movies[4])
    db.session.commit()

    movies[5].rate1 = 0.09 * 101
    movies[5].rate2 = 0.132 * 101
    movies[5].rate3 = 0.22156 * 101
    movies[5].rate4 = (1 - 0.09 - 0.132 - 0.22156) * 101
    db.session.add(movies[5])
    db.session.commit()

    movies[6].rate1 = 0.01 * 101
    movies[6].rate2 = 0.15256 * 101
    movies[6].rate3 = 0.25156 * 101
    movies[6].rate4 = (1 - 0.01 - 0.15256 - 0.25156) * 101
    db.session.add(movies[6])
    db.session.commit()

    movies[7].rate1 = 0.05 * 101
    movies[7].rate2 = 0.23 * 101
    movies[7].rate3 = 0.356 * 101
    movies[7].rate4 = (1 - 0.05 - 0.23 - 0.356) * 101
    db.session.add(movies[7])
    db.session.commit()

    movies[8].rate1 = 0.02 * 101
    movies[8].rate2 = 0.26 * 101
    movies[8].rate3 = 0.25156 * 101
    movies[8].rate4 = (1 - 0.02 - 0.26 - 0.25156) * 101
    db.session.add(movies[8])
    db.session.commit()

    movies[9].rate1 = 0.03 * 101
    movies[9].rate2 = 0.25 * 101
    movies[9].rate3 = 0.71 * 101
    movies[9].rate4 = (1 - 0.03 - 0.25 - 0.71) * 101
    db.session.add(movies[9])
    db.session.commit()

    movies[10].rate1 = 0.01 * 101
    movies[10].rate2 = 0.19 * 101
    movies[10].rate3 = 0.25156 * 101
    movies[10].rate4 = (1 - 0.01 - 0.19 - 0.25156) * 101
    db.session.add(movies[10])
    db.session.commit()

    movies[11].rate1 = 0.2 * 101
    movies[11].rate2 = 0.15256 * 101
    movies[11].rate3 = 0.25156 * 101
    movies[11].rate4 = (1 - 0.2 - 0.15256 - 0.25156) * 101
    db.session.add(movies[11])
    db.session.commit()

    movies[12].rate1 = 0.002 * 101
    movies[12].rate2 = 0.136 * 101
    movies[12].rate3 = 0.5693 * 101
    movies[12].rate4 = (1 - 0.002 - 0.136 - 0.5693) * 101
    db.session.add(movies[12])
    db.session.commit()

    movies[13].rate1 = 0.0996 * 101
    movies[13].rate2 = 0.1632* 101
    movies[13].rate3 = 0.25156 * 101
    movies[13].rate4 = (1 - 0.0996 - 0.1632 - 0.25156) * 101
    db.session.add(movies[13])
    db.session.commit()

    movies[14].rate1 = 0.01 * 101
    movies[14].rate2 = 0.3556 * 101
    movies[14].rate3 = 0.25156 * 101
    movies[14].rate4 = (1 - 0.01 - 0.3556 - 0.25156) * 101
    db.session.add(movies[14])
    db.session.commit()

    movies[15].rate1 = 0.025 * 101
    movies[15].rate2 = 0.156 * 101
    movies[15].rate3 = 0.251 * 101
    movies[15].rate4 = (1 - 0.025 - 0.156 - 0.251) * 101
    db.session.add(movies[15])
    db.session.commit()

    movies[16].rate1 = 0.12 * 101
    movies[16].rate2 = 0.16756 * 101
    movies[16].rate3 = 0.3156 * 101
    movies[16].rate4 = (1 - 0.12 - 0.16756 - 0.3156) * 101
    db.session.add(movies[16])
    db.session.commit()

    movies[17].rate1 = 0.03256 * 101
    movies[17].rate2 = 0.356 * 101
    movies[17].rate3 = 0.58 * 101
    movies[17].rate4 = (1 - 0.03256 - 0.356 - 0.58) * 101
    db.session.add(movies[18])
    db.session.commit()

    movies[18].rate1 = 0.02 * 101
    movies[18].rate2 = 0.08 * 101
    movies[18].rate3 = 0.5156 * 101
    movies[18].rate4 = (1 - 0.02 - 0.08 - 0.5156) * 101
    db.session.add(movies[18])
    db.session.commit()

    movies[19].rate1 = 0.03 * 101
    movies[19].rate2 = 0.17 * 101
    movies[19].rate3 = 0.352145 * 101
    movies[19].rate4 = (1 - 0.03 - 0.17 - 0.352145) * 101
    db.session.add(movies[19])
    db.session.commit()
if __name__ == '__main__' :
    manager.run()
