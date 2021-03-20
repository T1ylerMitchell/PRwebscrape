from googlesearch import search
import docx

searchInput = input()

print(searchInput)

result = search(searchInput, num_results=10)

mydoc = docx.Document()

for link in result:
    mydoc.add_paragraph(link)

mydoc.save("C:\\Users\\14794\\Desktop\\git\\reports\\report.docx")

print(result)
