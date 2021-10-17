import requests 
# 6c420424-62ad-4218-8b1f-d6cf2115facd
class jsnDrop(object):
    def __init__(self, tok = None, url = None) -> None:
        self.tok = tok
        self.url = url
    
    def create(self,table_name, example):
        # https://newsimland.com/~todd/JSON/?tok={"tok":"6c420424-62ad-4218-8b1f-d6cf2115facd","cmd":{"CREATE":"tblTest","EXAMPLE":{"PersonID  PK":"Todd","Score":21}}}
        payload = {'tok':'{"tok":"6c420424-62ad-4218-8b1f-d6cf2115facd","cmd":{"CREATE":"tblTest","EXAMPLE":{"PersonID  PK":"Todd","Score":21}}}'}
        # payload = {'tok':{"tok":"6c420424-62ad-4218-8b1f-d6cf2115facd","cmd":{"CREATE":"tblTest","EXAMPLE":{"PersonID  PK":"Todd","Score":21}}}}
        r = requests.get(self.url, payload)
        print(r.url)
        print(f"TEXT {r.text}")
        print(r.json())
