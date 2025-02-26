def procces(data,batchessize):
    datasize=len(data)
    for start in range(0,datasize,batchessize):
        end=min(start+batchessize,datasize)
        batch=data[start:end]
        print(f"processing data from {start}and {end}")
        print()
data=list(range(430))
batchsize=50
dataa=(batchsize,50)

