from email import message
import facebook_sdk as fb
#get access tocken

access_tocken = "EAAGWibRZAzKQBANCPajygM05I1S6yeSC83UXmwdQZBhHf2ESBW6s5O7h7LNMrBgi1tRnqrIF6vTbqOsVCpDTnhnwEV77LdbDfoDi9YjwVEyLVcc0DPHdotIYQdZABOgquhSb7est2SSPncu0ux6VlllDu2hZBBRIZBLdMCCZCAdfxcediZBVh6xNdfPP3EN0o9TzFusZBuuBRFDuPbDmG6r5"
#the graphic API allow you to read and write data to  and from the facebook social graph
asafb = fb.GraphAPI(access_tocken)
# post a message in the facebokk
asafb.put_object("me","feed", message = "hello this amazing technology")

#get a message in the facebook page

asafb.get_object("id that was generated") 
fb.put_like("my page id _my post id")

#post  PHOTO WITH CAPTIONS
asafb.put_photo(open("name.jpg","rb"),message = "automated message")


#COMMENT ON POST
asafb.put_object("116677775665_77887878787", "3535353ere", "feed", message = "this automated")

