def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if len(responseTimes)==0:
        return 0

    count=0
    total=responseTimes[0]
    for i in range(1,len(responseTimes)):
        avg=total/i
        if responseTimes[i]>avg:
          count+=1
        total+=responseTimes[i]
    return count
if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)