def mapper(arr):

    return [(word, 1) for word in arr]



if __name__ == "__main__":
    
    input_data_path = "word_count_data.txt"
    output_data_path = "test.out"

    with open(input_data_path, 'r') as inp:
        lines = inp.readlines()
        
        rows = len(lines)
        
        with open(output_data_path, 'w') as out:

            out.write("[\n\t")

            rows = len(lines)
            for j, line in enumerate(lines):
                line = line.strip()
                res = mapper(line.split(" "))
            
                cols = len(res)
                for i, item in enumerate(res):
                    if j == rows - 1 and i == cols - 1:
                        out.write(f'("{item[0]}", {item[1]})')
                    else:
                        out.write(f'("{item[0]}", {item[1]}),\n\t')
                
            out.write("\n]")