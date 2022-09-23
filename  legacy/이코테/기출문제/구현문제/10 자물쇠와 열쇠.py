def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] #결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]
    return result

#자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = True
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))