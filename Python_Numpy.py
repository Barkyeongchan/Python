import numpy as np
a = np.array([1,2,3])
print(a)
print(a.shape) #형태 / 튜플로 반환
print(a.dtype) #원소의 타입
print(a.ndim) #배열의 차원
print(a.itemsize) #원소의 메모리 크기 / byte로 표시
print(a.size) #원소의 갯수

student_mid = [70, 85, 90, 75]
student_fin = [90, 65, 70, 85]
student_sum = student_mid + student_fin
print(student_sum) # [70, 85, 90, 75, 90, 65, 70 ,85] : 리스트끼리 합한 결과값
# print(student_sum / 2) # 오류! 리스트는 나누기를 지원하지 않음

student_mid = np.array([70, 85, 90, 75]) # 넘파이 다차원 배열은 행열과 같이 계산 할 수 있다.
student_fin = np.array([90, 65, 70, 85])
student_sum = student_mid + student_fin
print(student_sum) # [160, 150, 160, 160] : 행열 연산이 진행된 결과값
print(student_sum / 2) # 넘파이 배열은 나누기 연산을 지원함 / 각 원소에 연산 적용

a = np.array([1,2,3,4]) #리스트
b = np.array([1,2,3,4]) #튜플
c = np.array(range(4)) # 레인지 형태로 가능