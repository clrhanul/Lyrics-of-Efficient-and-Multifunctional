# Project
## Why
이 프로젝트는 `.lyx` 확장자를 만드는 프로젝트 입니다.
`.lyx`는 `Lyrics Extended`의 약자입니다. (원래는 `Lyrics of Efficient and Multifunctional`를 줄여 `.lem`로 하려 했으나, ChatGPT의 답변 중 `.lyx`가 더 멋져보여 이걸로 채택했습니다.)
이 프로젝트는 기능이 많고, 효율적인 가사 및 자막 파일을 만드는 것이 목적입니다.

## After
현재는 프로젝트 주인이 실력이 안되서 Python 버전으로만 encode, decode 스크립트를 제시했으나, 나중에는 C, Java 등 Low Level의 코드도 작성할 예정입니다.

# 파일 형식
파일은 가장 크게 아래의 세 부분으로 나뉩니다.
 - 이 형식의 가장 첫 1바이트는 현재 파일의 포맷 버전을 나타냅니다.
 - 그 다음으로 METADATA가 옵니다.
 - 이후 암호화된 CONTENT가 등장합니다.
파일 형식에 대한 문서는 아래의 하이퍼링크를 참조하세요.
[ [.lrx(v_1.0)](./docs/file-format/V1.0-LRX.md) | ... ]

## METADATA
METADATA는 BLOCK 단위로 처리해야하는 구조입니다.
PREFIX로 시작하며, 이 PREFIX는 항상 4비트로 구성되어 있습니다.

### METADATA PREFIX
0. `1111` : 모든 메타데이터를 읽었음을 나타내는 PREFIX입니다. 이후엔 CONTENT가 등장합니다.
1. `0000` : 아무 의미가 없는 PREFIX입니다. 그냥 넣고 싶었습니다. 이 PREFIX를 읽으면 그냥 다음 PREFIX로 건너뜁니다.
### METADATA BLOCK

## CONTENT


# Algorithm
이 단락은 해당 확장자가 어느 방법으로 암호화되고 복호화되는지를 나타내는 단락입니다.
## Encode
1. 허프만 코드를 사용하여 암호화합니다.

## Decode
1. 허프만 코드를 사용하여 복호화합니다.
