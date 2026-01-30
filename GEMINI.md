## 목표

- Excel 파일을 CSV 파일로 변환하는 프로그램을 개발
- python3로 개발

### 코드 규칙

- 가독성과 유지보수성이 높은 코드를 작성한다.
- 성능을 고려하여 코드를 작성한다.
- python3의 best practice를 준수한다.
- python3의 Naming Convention을 준수한다.

### 기능

- excel2csv.py 파일을 실행한다.
- Excel 파일을 CSV 파일로 변환한다.
- excel2csv.py ExcelFile.xlsx(xls) 파라미터로 Excel 파일의 시트 목록을 출력한다. (출력포맷: Index. SheetName.csv)
- excel2csv.py ExcelFile.xlsx(xls) <SheetIndex 또는 SheetName> 과 같이 인덱스 또는 시트 이름을 지정하여 Excel 파일의 sheet를 csv로 출력한다.
  - 인덱스 지정 시 파일명: Index_SheetName.csv (예: 1_Sheet1.csv)
  - 시트 이름 지정 시 파일명: SheetName.csv (예: Sheet1.csv)
- -a 또는 --all 옵션을 사용하여 모든 시트를 각각의 CSV 파일로 일괄 변환한다.
- csv 파일의 기본 인코딩은 utf-8이다. 기본 인코딩 변경을 위해서는 -e 또는 --encoding 옵션을 사용한다.
- csv 파일의 기본 구분자는 ','이다. 기본 구분자 변경을 위해서는 -s 또는 --separator 옵션을 사용한다.
- csv 파일의 기본 인용 문자는 '"'이다. 기본 인용 문자 변경을 위해서는 -q 또는 --quotechar 옵션을 사용한다.
- csv 파일의 기본 라인 종결 문자는 '\n'이다. 기본 라인 종결 문자 변경을 위해서는 -l 또는 --line-terminator 옵션을 사용한다.
- -D 또는 --date-format 옵션을 사용하여 날짜 형식을 지정한다. (예: %Y-%m-%d)
- --no-header 옵션을 사용하여 CSV 출력 시 첫 번째 줄(헤더)을 제외한다.
- -h 또는 --help 옵션을 사용하여 도움말을 출력한다.
- -v 또는 --version 옵션을 사용하여 버전을 출력한다.
- -o 또는 --output 옵션을 사용하여 출력 파일의 이름을 지정한다. (일괄 변환 시에는 무시되거나 디렉토리 지정용으로 사용될 수 있음)
- csv 출력시 구분자를 포함한 문자열이 발견되면 구분자를 인용 문자로 처리하고, 인용 문자를 포함한 문자열이 발견되면 인용 문자를 이스케이프 문자로 처리한다.
