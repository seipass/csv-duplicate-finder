import argparse,csv,json,sys
def transform(rows):
    seen=set(); duplicates=[]
    for row in rows:
        key=tuple(sorted(row.items()))
        if key in seen: duplicates.append(row)
        else: seen.add(key)
    return duplicates

def main():
    parser=argparse.ArgumentParser(description='CSV duplicate row finder')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    reader=csv.DictReader(source.splitlines())
    result=transform(list(reader))
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
