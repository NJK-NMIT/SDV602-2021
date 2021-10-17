from model.network.jsn_drop_service import jsnDrop

class UserManager(object):
    def __init__(self) -> None:
        super().__init__()
        self.jsnDrop = jsnDrop("6c420424-62ad-4218-8b1f-d6cf2115facd","https://newsimland.com/~todd/JSON")
        self.jsnDrop.create("tblUser",{"PersonID  PK":"Todd","Score":21})

