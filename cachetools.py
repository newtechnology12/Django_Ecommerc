from markupsafe import Markup, escape
# escape replaces special characters and wraps in Markup
result=escape("<script>alert(document.cookie);</script>")
print(result)
# wrap in Markup to mark text "safe" and prevent escaping

result= Markup("<strong>Hello</strong>")
print(result)