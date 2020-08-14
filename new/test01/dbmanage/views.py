from django.shortcuts import render
import sqlite3
def list(request):
    data =request.GET.copy()
    with sqlite3.connect("db.sqlite3") as con:
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select*from economic")
        data['rows']=cur.fetchall()
    return render(request,'list.html',context=data)
# Create your views here.
