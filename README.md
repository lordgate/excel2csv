# excel2csv

Excel 파일(.xlsx, .xls)을 CSV 파일로 변환하는 Python 명령줄 도구입니다.

## 특징

- **시트 목록 확인**: 엑셀 파일 내의 시트 목록을 조회할 수 있습니다.
- **선택적 변환**: 인덱스 번호 또는 시트 이름으로 특정 시트만 변환할 수 있습니다.
- **일괄 변환**: 파일 내 모든 시트를 한 번에 각각의 CSV 파일로 변환할 수 있습니다.
- **강력한 옵션**: 인코딩, 구분자(Separator), 날짜 포맷, 헤더 제외 등 다양한 옵션을 지원합니다.

## 설치

### 1. Python 3 설치

이 도구는 Python 3 환경에서 실행됩니다. Python이 설치되어 있지 않다면 아래 방법을 참고하여 설치하세요.

- **Windows**: [Python 공식 홈페이지](https://www.python.org/downloads/windows/)에서 설치 프로그램을 다운로드하여 실행합니다. 설치 시 "Add Python to PATH" 옵션을 반드시 체크하세요.
- **macOS**: [Python 공식 홈페이지](https://www.python.org/downloads/macos/)에서 설치하거나 Homebrew를 사용하여 설치할 수 있습니다.

  ```bash
  brew install python
  ```

- **Linux (Ubuntu/Debian)**:

  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

### 2. 라이브러리 설치

`requirements.txt`에 명시된 필수 라이브러리(`pandas`, `openpyxl`, `xlrd`)를 설치해야 합니다. 터미널(또는 명령 프롬프트)에서 프로젝트 폴더로 이동한 후 아래 명령어를 실행하세요.

```bash
pip install -r requirements.txt
```

> **참고**: 만약 `pip` 명령어가 동작하지 않는다면 `pip3` 또는 `python3 -m pip`를 사용해 보세요.

## 사용법

```bash
python3 excel2csv.py [옵션] 입력파일 [시트]
```

### 1. 시트 목록 확인

인자 없이 엑셀 파일만 지정하면 포함된 시트 목록을 출력합니다.

```bash
python3 excel2csv.py data.xlsx
```

### 2. 특정 시트 변환

시트 인덱스(1부터 시작) 또는 시트 이름을 지정하여 변환합니다.

```bash
# 첫 번째 시트 변환
python3 excel2csv.py data.xlsx 1

# "Sheet1" 시트 변환
python3 excel2csv.py data.xlsx "Sheet1"

# 출력 파일명 지정 (-o)
python3 excel2csv.py data.xlsx 1 -o result.csv
```

### 3. 모든 시트 일괄 변환 (-a)

모든 시트를 각각의 CSV 파일로 변환합니다. 파일명은 `시트명.csv`가 됩니다.

```bash
python3 excel2csv.py data.xlsx -a
```

## 옵션 설명

| 옵션 | 설명 | 기본값 |
| --- | --- | --- |
| `-h`, `--help` | 도움말 출력 | |
| `-v`, `--version` | 버전 정보 출력 | |
| `-a`, `--all` | 모든 시트를 CSV로 일괄 변환 | |
| `-o`, `--output` | 출력 파일 이름 지정 (단일 시트 변환 시) | 자동 생성 |
| `-e`, `--encoding` | CSV 파일 인코딩 | `utf-8` |
| `-s`, `--separator` | 필드 구분자 | `,` (쉼표) |
| `-q`, `--quotechar` | 인용 문자 (데이터 내 구분자 포함 시 감싸는 문자) | `"` (따옴표) |
| `-l`, `--line-terminator` | 줄바꿈 문자 | `\n` |
| `-D`, `--date-format` | 날짜 형식 지정 (예: `%Y-%m-%d`) | 기본 형식 |
| `--no-header` | 첫 번째 줄(헤더)을 제외하고 데이터만 출력 | |

## 예시

**날짜 형식을 `YYYY-MM-DD`로 지정하고 헤더를 제외하여 저장:**

```bash
python3 excel2csv.py data.xlsx 1 -D "%Y-%m-%d" --no-header -o clean_data.csv
```

**텍스트 구분자로 파이프(`|`) 사용:**

```bash
python3 excel2csv.py data.xlsx 1 -s "|"
```
