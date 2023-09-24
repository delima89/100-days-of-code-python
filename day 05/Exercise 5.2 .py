student_scores = input("escreva a maior nota do seus alunos ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
maxima=0
for nota in student_scores:
    if maxima < nota:
        maxima=nota
    
print(f"o aluno com a maior nota da turma é: {maxima}") 