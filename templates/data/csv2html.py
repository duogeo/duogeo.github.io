#!/bin/bash
import csv

def printrow(row):
    print("<tr>")
    print("<td>"+row[0].strip()+"</td>")
    print("<td>"+"<div class=\"tym-vysledky\">"+"<div>"+row[1].strip()+"</div>"+"<div>"+row[2].strip()+"</div>"+"</div>"+"</td>")
    for data in row[3:]:
        print("<td>"+data.strip()+"</td>")
    print("</tr>")

with open('ss.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    print("<table class=\"tym-table\">")
    print("<tr>")
    print("<th></th>")
    print("<th>Tým</th>")
    print("<th>1</th>")
    print("<th>2</th>")
    print("<th>3</th>")
    print("<th>4</th>")
    print("<th>5</th>")
    print("<th>6</th>")
    print("<th>Součet</th>")
    print("</tr>")
    for row in reader:
        printrow(row)
    print("</table>")
