def stream_test_case():
    streams = ['{}','{{{}}}','{{},{}}','{{{},{},{{}}}}','{<a>,<a>,<a>,<a>}',\
               '{{<ab>},{<ab>},{<ab>},{<ab>}}','{{<!!>},{<!!>},{<!!>},{<!!>}}',\
               '{{<a!>},{<a!>},{<a!>},{<ab>}}']
    scores = [1,6,5,16,9,9,3]

    for stream in streams:
        stream_processing(stream)

def stream_processing(stream):
    print(stream)
    stream = stream.split('!')
    stream_size = len(stream)
    i = 0
    while stream_size-1>i:
        if stream[i]:
            stream[i+1] = stream[i+1][1:]
        else:
            stream.pop(i)
            stream_size = len(stream)
        i += 1
    stream = "".join(stream)
    print(stream,'\n')

stream_test_case()
