# <div style="text-align: center;">hard-data-transmission</div>
<!-- <p align="center">
  <img src="/static/icon.png"  width="256" height="256" alt="nuxt-firebase logo">
</p>
 -->
## Description
IoTコンポストトイレのハードウェアに組み込むプログラム<br>
Firestoreへのデータの追加処理とFirebaseにアクセスするための認証用プログラム

**This repository sends requests to the back-end server of [back-firebase-functions](https://github.com/inct-compost/back-firebase-functions) to authenticate and add data**

## Requirement
| name | version |
| ------------- | ------------- |
| python(global) | 3.x |
| netifaces | 0.11.0 |

## Getting Started
### 1. Install package
```powershell
pip install netifaces
```

### 2. Add json files
#### 2-1. touch file
```powershell
cd json 
```

```powershell
touch login_params.json token.json
```

#### 2-2. Edit json file
**`login_params.json`**
```json
{
  "id": "[hardware-id]",
  "pass": "[password]"
}
```

**`token.json`**
```json
{}
```

## How to use
### Add sensing data
```powershell
python main.py add -i [temp] [hum]
```
