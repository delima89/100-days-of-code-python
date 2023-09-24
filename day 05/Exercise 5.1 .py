student_heights = input("qual é o tamanho dos seus alunos").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

conta=0
tamanho=0
for alunos in student_heights :
     tamanho+=alunos
     conta+=1
media=tamanho/conta
print("a media do tamnaho do seus alunos e",round(media+0.5))

