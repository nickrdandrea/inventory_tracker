from app import create_app, db
from app.models import Alert, Item, User, Vendor

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
                'db': db, 
                'Alert': Alert, 
                'Item': Item, 
                'User': User, 
                'Vendor': Vendor
            }

if __name__ == "__main__":
    app.run()
