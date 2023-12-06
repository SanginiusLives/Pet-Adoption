from models import Pets, db
from app import app


app.app_context().push()
db.drop_all()
db.create_all()

winter = Pets(name="Winter", species="Dog", age=2, available=False)
parsley = Pets(name="Parsley", species="Gecko", age=2, available=False)
bruno = Pets(name="Bruno", species="Dog", age=1, available=True)

db.session.add(winter)
db.session.add(parsley)
db.session.add(bruno)

db.session.commit()