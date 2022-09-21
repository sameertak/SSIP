import requests

data = {
    "res1" : "A",
    "res2" : "B",
    "res3" : "asidygfasiudhashdosah dashdiuasndiasyduasdas dsibsiducbds said ci iasuasniuasbncbasij casi ciasb sa"
}
answer = requests.post('https://otplogin.pythonanywhere.com/feedback/form/', json=data)