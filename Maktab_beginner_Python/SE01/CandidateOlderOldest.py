ValidAge=range(10,91)
num_array=list()
CandidateAge=int(input())
num_array=[CandidateAge]
#num_array.insert(CandidateAge,0)
while CandidateAge !=-1 and CandidateAge in ValidAge:
    CandidateAge=int(input())
    num_array.append(int(CandidateAge))
num_array=sorted(num_array, reverse=True)
print(num_array[0],num_array[1])