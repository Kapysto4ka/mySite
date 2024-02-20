from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main Page</title>
</head>
<body>
  <p>Choose destination</p>
  <ul>
    <li><a href="/groups">Navigate to groups</a></li>
    <li><a href="/students">Navigate to students</a></li>
  </ul>
</body>
</html>''')