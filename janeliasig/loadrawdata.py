def loadRawData(filename, num_elements = float("inf"), sourcedataformat = 'int8', target_dataformat = 'int8'):

    #dirinfo = dir(filename)
    file_size_bytes = os.path.getsize(filename)
   
    def doInt8(): 
        #bytesperelement = 1
        return 1
    def doInt16():
        #bytesperelement = 2
        return 2
    def doInt32():
        #bytesperelement = 4
        return 4
    def doInt64():
        #bytesperelement = 8
        return 8
    def error():
        print "Your input has not been recognized"
    formats = {
        'int8': doInt8(),
        'uint8': doInt8(),
        'int16': doInt16(),
        'uint16': doInt16(),
        'int32': doInt32(),
        'uint32': doInt32(),
        'int64': doInt64(),
        'uint64': doInt64()}
    
    bytes_per_element = formats.get(sourcedataformat, 'int8')
    
    num_file_elements = math.floor(file_size_bytes / bytes_per_element)
    
    num_elements = min(num_elements, num_file_elements)
    data = np.zeros(num_elements, target_dataformat)
    
    chunk_size_bytes = 50e6
    chunk_size_elements = chunk_size_bytes / bytes_per_element
    
    fileID = open(filename, 'rb')
    
    for iter in range(1, int(math.floor(num_elements/chunk_size_elements))):
         data[chunk_size_elements*(iter-1)+1: chunk_size_elements*iter] = np.fromfile(fileID, sourcedataformat, chunk_size_elements)
    
    remaining_elements = int(num_elements%chunk_size_elements)
    data[-1 - remaining_elements+1:-1] = np.fromfile(fileID, sourcedataformat, remaining_elements - 1)
   
    return data
    fileID.close()
