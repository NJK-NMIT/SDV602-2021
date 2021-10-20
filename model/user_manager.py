from model.network.jsn_drop_service import jsnDrop
from time import gmtime  #  gmt_time returns UTC time struct frim 

class UserManager(object):

    def now_time_stamp(self):
        time_now = gmtime()
        timestamp_str = f"{time_now.tm_year}:{time_now.tm_mon}:{time_now.tm_mday}:{time_now.tm_hour}:{time_now.tm_min}:{time_now.tm_sec}"
        return timestamp_str
 

    def __init__(self) -> None:
        super().__init__()
        self.currentUser = ""
        self.current_status = ""

        self.jsnDrop = jsnDrop("6c420424-62ad-4218-8b1f-d6cf2115facd","https://newsimland.com/~todd/JSON")

        # SCHEMA Make sure the tables are  CREATED - jsnDrop does not wipe an existing table 
        result = self.jsnDrop.create("tblUser",{"PersonID PK":"A_LOOONG_NAME",
                                                "Password":"A_LOOONG_PASSWORD",
                                                "Status":"STATUS_STRING"})

        result = self.jsnDrop.create("tblChat",{"PersonID PK":"A_LOOONG_NAME",
                                                "DESNumber":"A_LOOONG_DES_ID",
                                                "Chat":"A_LOONG____CHAT_ENTRY",
                                                "Time": self.now_time_stamp()})

        # self.test_api()

    def register(self, user_id, password):
        result = self.jsnDrop.select("tblUser",f"PersonID = '{user_id}'") # Danger SQL injection attack via user_id?? Is JsnDrop SQL injection attack safe??
        if( "DATA_ERROR" in self.jsnDrop.jsnStatus):
            result = self.jsnDrop.store("tblUser",[{'PersonID':user_id,'Password':password,'Status':'Registered'}])
            self.currentUser = user_id
            self.current_status = 'Registered'
        else:
            result = "User Exists"

        return result

    def test_api(self):
        result = self.jsnDrop.create("tblTestUser",{"PersonID PK":"Todd","Score":21})
        print(f"Create Result from UserManager {result}")

        self.jsnDrop.store("tblTestUser",[{"PersonID":"Todd","Score":21},{"PersonID":"Jane","Score":201}])
        print(f"Store Result from UserManager {result}")

        result = self.jsnDrop.all("tblTestUser")
        print(f"All Result from UserManager {result}")

        result = self.jsnDrop.select("tblTestUser","Score > 200") # select from tblUser where Score > 200
        print(f"Select Result from UserManager {result}")

        result = self.jsnDrop.delete("tblTestUser","Score > 200") # delete from tblUser where Score > 200
        print(f"Delete Result from UserManager {result}")

        result = self.jsnDrop.drop("tblTestUser")
        print(f"Drop Result from UserManager {result}")



        

