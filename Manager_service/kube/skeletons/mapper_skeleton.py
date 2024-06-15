
if __name__ == "__main__":

    import argparse
    from mapper_input import mapper

    parser = argparse.ArgumentParser(description="Process input and output paths")
    parser.add_argument('-i', '--input', type=str, default="word_count_data.txt", help='Input data file path')
    parser.add_argument('-o', '--output', type=str, default="mapper.out", help='Output data file path')
    args = parser.parse_args()
    
    # Should be changed
    input_data_path = args.input
    output_data_path = args.output

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

