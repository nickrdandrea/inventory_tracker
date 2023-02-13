# from old_app import create_app, db
# from old_app.models import Alert, Item, User, Vendor
# from old_app.updater.updater import updater
# from old_app.db_utils import add_vendor, drop_records, search_item
from app import create_app

app = create_app()
# @app.shell_context_processor
# def make_shell_context():
#     return {
#             "db": db,
#             "Item": Item, 
#             "User": User, 
#             "Vendor": Vendor,
#             "add_vendor": add_vendor,
#             "drop_records": drop_records,
#             "search_item": search_item,
#             "updater": updater
#             }
# @app.shell_context_processor
# def make_shell_context():
#     return {

#     }
if __name__ == "__main__":
    app.run()
