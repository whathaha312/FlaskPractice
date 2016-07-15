from  WEB import app,db
from flask_script import Manager
from WEB.models import User,Image,Comment
import random,hashlib
manager=Manager(app)



def get_image_url():
    return 'https://www.baidu.com/img/bd_logo1.png' #'http://images/nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        m=hashlib.md5()
        m.update('a'+str(i)+'')
        password=m.hexdigest()
        db.session.add(User('USER'+str(i),password))
        for j in range(0,10):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('this is '+str(k),1+3*i+j,i+1))
    db.session.commit()
    for i in range(30,100,2):
        user=User.query.get(i)
        user.username='new'+user.username
    db.session.commit()
    print Image.query.order_by('id desc').limit(10).all();

if __name__== '__main__':
    manager.run();