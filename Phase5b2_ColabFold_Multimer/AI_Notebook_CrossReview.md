# UFoE Phase 5b-2/5c: AI 노트북 교차 리뷰
# 4개 AI 생성 노트북 비교 분석
# 2026-02-13 Young Kang + Claude Code

---

## 0. 리뷰 대상

| # | 파일명 | 생성 AI | 버전 |
|---|--------|---------|------|
| 1 | `UFoE_Phase5b2_ColabFold_Multimer.ipynb` | **Claude Code** (현재 세션) | Phase 5b-2 |
| 2 | `UFoE_Phase5b2_ColabFold_Multimer_claude.ipynb` | **Claude** (다른 세션) | Phase 5b-2 |
| 3 | `Phase5c_ColabFold_Multimer_Genspark.ipynb` | **Genspark** | Phase 5c |
| 4 | `Phase_5c_ColabFold_Multimer.ipynb` | **불명** (ChatGPT/Gemini 추정) | Phase 5c |

---

## 1. 서열 정확성 — 가장 치명적인 차이

### 확정 서열 (규칙 기반 검증 완료)

| Group | 서열 | 길이 | 곤% | 건% |
|-------|------|------|-----|-----|
| A (WT) | RMKQLEDKVEELLSKNYHLENEVARLKKLVGER | **33aa** | 33% | 45% |
| B (곤↑) | LMKQLEDIVEELLSLNYHLEINEVALKKLLGEL | **33aa** | 48% | 30% |
| C (건↑) | REKKLEDKEEKLLSKEYKLENEEAKLKKLEGKR | **33aa** | 21% | 67% |

### 각 노트북의 서열 비교

```
확정 Group A: RMKQLEDKVEELLSKNYHLENEVARLKKLVGER (33aa)
확정 Group B: LMKQLEDIVEELLSLNYHLEINEVALKKLLGEL (33aa)
확정 Group C: REKKLEDKEEKLLSKEYKLENEEAKLKKLEGKR (33aa)
```

#### 노트북 1 (Claude Code — 현재 세션) ✅
```
A: RMKQLEDKVEELLSKNYHLENEVARLKKLVGER  (33aa) ✅ 확정본 일치
B: LMKQLEDIVEELLSLNYHLEINEVALKKLLGEL  (33aa) ✅ 확정본 일치
C: REKKLEDKEEKLLSKEYKLENEEAKLKKLEGKR  (33aa) ✅ 확정본 일치
```

#### 노트북 2 (Claude 다른 세션) ⚠️
```
A: RMKQLEDKVEELLSKNYHLENEVARLKKLVGER  (33aa) ✅
B: LMKQLEDIVEELLSLNYHLEINEVALKKLLGEL  (33aa) ✅
C: REKSLEDKVEELLSKEYKLENEVERKKLEGEK   (31aa) ❌ 2잔기 짧음 + 다른 서열
```
**문제**: Group C가 31aa (33aa여야 함). e,g 위치 변환 규칙이 제대로 적용되지 않음.

#### 노트북 3 (Genspark) ❌❌❌ 치명적
```
A: RMKQLEDKVEELLSKNYHLENEVARLKKLVGER  (33aa) ✅
B: LMKQLEDIVEELLSLNYHLEINEVALKKLLGEL  (33aa) ✅
C: REKSLEDKVEELLSKEYKLENEVERKKLEGEK   (31aa) ❌ 노트북2와 동일 오류
```
**심각한 문제**: Group C 서열이 31aa + 곤감리건 변환 불완전

#### 노트북 4 (Phase_5c 불명) ❌❌❌❌ 실험 무효
```
A: MKQLEDKVEELLSKNYHLENEVARLKKLVGER  (32aa!) ❌ 첫 R 누락
B: MKQLEDKVLELLSKNYHLLNEVARLKKLVGER  (32aa!) ❌ 완전히 다른 변이체
C: MKQLEDKVEELLSKNYHLENEVARLKKLVGER  (32aa!) ❌ = A와 동일!!!
```
**치명적 결함**:
1. 모든 서열이 32aa (R 누락)
2. **Group C = Group A** — 변이 자체가 없음 → 실험 무의미
3. Group B 변이도 확정본과 완전히 다름

### 서열 정확성 판정

| 노트북 | A 서열 | B 서열 | C 서열 | 실험 유효성 |
|--------|--------|--------|--------|------------|
| 1 (Claude Code) | ✅ 33aa | ✅ 33aa | ✅ 33aa | ✅ **유효** |
| 2 (Claude 타세션) | ✅ 33aa | ✅ 33aa | ❌ 31aa | ⚠️ C 재검증 필요 |
| 3 (Genspark) | ✅ 33aa | ✅ 33aa | ❌ 31aa | ⚠️ C 재검증 필요 |
| 4 (Phase_5c 불명) | ❌ 32aa | ❌ 다른 변이 | ❌ A와 동일 | ❌ **실험 무효** |

---

## 2. Heptad Register 매핑

### 확정 Register
```
Position:  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
Heptad:    d  e  f  g  a  b  c  d  e  f  g  a  b  c  d  e  f  g  a  b  c  d  e  f  g  a  b  c  d  e  f  g  a
```

| 노트북 | Register 방식 | 시작 위치 | 정확도 |
|--------|-------------|----------|--------|
| 1 (Claude Code) | 하드코딩 문자열 `'defgabcdefg...'` | d (pos 1) | ✅ 정확 |
| 2 (Claude 타세션) | `get_heptad_registry()` 함수 | d (start_position='d') | ✅ 정확 |
| 3 (Genspark) | 사용하지 않음 | — | ❌ register 미적용 |
| 4 (Phase_5c 불명) | `heptad_pattern[(i-1)%7]` | a (pos 2부터) | ❌ **1 위치 밀림** |

**노트북 4의 register 오류**:
```python
heptad_pattern = 'abcdefg'
for i in range(len(sequence)):
    heptad_pos = heptad_pattern[(i - 1) % 7] if i >= 1 else '-'
```
- pos 0 = '-' (무시), pos 1 = 'a', pos 2 = 'b' ...
- 실제: pos 1 = d, pos 2 = e, pos 3 = f ...
- **a,d 위치가 완전히 틀림** → 코어 패킹 분석 무의미

---

## 3. ColabFold 실행 설정

| 설정 | 1 (Claude Code) | 2 (Claude) | 3 (Genspark) | 4 (Phase_5c) |
|------|-----------------|------------|--------------|-------------|
| 모델 수 | 5 | 5 | 5 | 5 |
| recycles | 3 | 3 | 3 | 3 |
| model_type | multimer_v3 | multimer_v3 | multimer_v3 | multimer_v3 |
| AMBER relax | 미사용 | 사용 (--amber) | 미사용 | 사용 |
| templates | 미사용 | 사용 (--templates) | 미사용 | 미사용 |
| FASTA 형식 | `seq:seq` (✅) | `seq:seq` (✅) | `seq:seq` (✅) | 별도 >ChainA/>ChainB (❌) |
| 배치 실행 | 단일 배치 | 그룹별 개별 | Python API 호출 | 그룹별 개별 |

**노트북 4 FASTA 형식 오류**:
```
>A_WT_ChainA
MKQLEDKVEELLSKNYHLENEVARLKKLVGER
>A_WT_ChainB
MKQLEDKVEELLSKNYHLENEVARLKKLVGER
```
이 형식은 ColabFold에서 multimer로 인식되지 않을 수 있음. 올바른 형식:
```
>A_WT
RMKQLEDKVEELLSKNYHLENEVARLKKLVGER:RMKQLEDKVEELLSKNYHLENEVARLKKLVGER
```

---

## 4. 분석 함수 비교

### 4.1 Salt Bridge 검출

| 항목 | 1 (Claude Code) | 2 (Claude) | 3 (Genspark) | 4 (Phase_5c) |
|------|-----------------|------------|--------------|-------------|
| inter-chain 전용 | ✅ | ✅ | ✅ (structure.get_chains) | ✅ |
| 양방향 검출 (A→B, B→A) | ✅ | ✅ | 단방향 (E/D→K/R만) | ✅ |
| canonical e-g' 분류 | ✅ (heptad 기반) | ✅ (e_set/g_set) | ❌ 없음 | ❌ 없음 |
| 중복 제거 | ✅ (unique dict) | ❌ 없음 | ❌ 없음 | ❌ 없음 |
| 원자 수준 거리 | ✅ (OE1,OE2,NZ 등) | ✅ | ❌ 모든 원자 쌍 | ✅ |
| cutoff | 4.0A | 4.0A | 4.0A | 4.0A |

**노트북 3의 salt bridge 과다 검출 위험**:
```python
for atomA in resA:     # GLU의 모든 원자 (N, CA, C, O, CB, CG, CD, OE1, OE2)
    for atomB in resB:  # LYS의 모든 원자 (N, CA, C, O, CB, CG, CD, CE, NZ)
        if atomA - atomB < cutoff:
            salt_bridges += 1
            break
```
CA-NZ 거리도 4A 이내면 카운트 → 심각한 과대평가. 주쇄 원자까지 포함.

### 4.2 Core Packing (Cb-Cb)

| 항목 | 1 (Claude Code) | 2 (Claude) | 3 (Genspark) | 4 (Phase_5c) |
|------|-----------------|------------|--------------|-------------|
| 대상 위치 | a,d (하드코딩) | a,d (heptad 함수) | 미구현 (빈 함수) | d만 (register 틀림) |
| 비교 종류 | a↔a', d↔d', a↔d', d↔a' | d↔d', a↔a', a↔d' | cb_distance만 정의 | d↔d'만 |
| same-heptad 비교 | ✅ (동일 위치 i↔i') | ✅ (details 포함) | ❌ | ❌ |
| Gly fallback (CB→CA) | ✅ | ✅ | ✅ | ✅ |
| 통계 | min/mean/std/n | mean/std/min/max/values | — | mean/std |

**노트북 3**: `cb_distance()` 함수만 정의하고 실제 분석 코드가 없음. 불완전.
**노트북 4**: heptad register가 1칸 밀려있어 d 위치가 실제로는 e 위치를 측정함.

### 4.3 Crossing Angle

| 항목 | 1 (Claude Code) | 2 (Claude) | 3 (Genspark) | 4 (Phase_5c) |
|------|-----------------|------------|--------------|-------------|
| 방법 | PCA (eigh) | PCA + DSSP fallback | SVD (vh[0]) | PCA (eig) |
| DSSP 활용 | ❌ | ✅ (helix only) | ❌ | ❌ |
| parallel/anti 판별 | ✅ (cos > 0) | ✅ | ❌ | ✅ (>90° 보정) |
| inter-helix distance | ✅ | ❌ | ❌ | ❌ |
| coiled-coil 판정 | ✅ (<30° + parallel) | ❌ | ❌ | ❌ |

**노트북 2 (Claude)의 DSSP 접근**: 가장 정교함. helix residue만 골라서 PCA → 비-helix 잔기에 의한 노이즈 제거.
**노트북 4**: `np.linalg.eig` 사용 (복소수 가능성) vs `np.linalg.eigh` (대칭행렬, 실수 보장) — 공분산 행렬은 대칭이므로 `eigh`가 더 안전.

### 4.4 추가 분석

| 분석 | 1 (Claude Code) | 2 (Claude) | 3 (Genspark) | 4 (Phase_5c) |
|------|-----------------|------------|--------------|-------------|
| SASA burial_ratio | ✅ | ✅ (곤감리건별) | ❌ | ❌ |
| Oligomeric state | ❌ | ✅ (cdist + 접촉 수) | ❌ | ❌ |
| pTM/ipTM 추출 | ✅ (JSON scores) | ❌ | ❌ | ❌ |
| 나이테 순서 검증 | ❌ | ✅ (곤<리<건) | ❌ | ❌ |
| 시각화 | ✅ (py3Dmol) | ✅ (matplotlib) | ❌ | ✅ (py3Dmol + matplotlib) |
| ESMFold 대조 | ✅ (내장 비교표) | ❌ | ❌ | ❌ |

---

## 5. 판정 기준 비교

### 노트북 1 (Claude Code)
```
곤 코어: B d↔d' ≤ A d↔d'
건 표면: C salt ≥ A + C burial > A
균형:    WT angle 18-25°
```

### 노트북 2 (Claude 타세션)
```
곤 코어: B d↔d' < A d↔d' < C d↔d' (3-way 비교)
건 표면: A salt ≥ C salt ≥ B salt (canonical 기준)
균형:    WT angle 15-28° (넓은 범위)
+ 추가:  C oligomeric state (dimer 유지?)
+ 추가:  SASA 나이테 곤<리<건
```

### 노트북 3 (Genspark)
```
(판정 기준 없음 — 함수만 정의하고 판정 코드 없음)
```

### 노트북 4 (Phase_5c)
```
A: salt 4-6, d↔d' 6.0-6.5A, angle 18-25°
B: salt 2-4, d↔d' 5.5-6.0A, angle 25-35°
C: salt ≤A, d↔d' >7.0A, angle >40°
```
기준이 있지만 register 오류로 실제 측정값이 틀릴 것.

---

## 6. 종합 등급

### 점수표 (각 10점 만점)

| 항목 | 1 (Claude Code) | 2 (Claude) | 3 (Genspark) | 4 (Phase_5c) |
|------|:---:|:---:|:---:|:---:|
| 서열 정확성 | **10** | 7 | 7 | **1** |
| Heptad register | **10** | **10** | 3 | **2** |
| ColabFold 설정 | 9 | **10** | 7 | 6 |
| Salt bridge 분석 | **10** | 9 | 3 | 7 |
| Core packing 분석 | **10** | **10** | 2 | 4 |
| Crossing angle 분석 | 9 | **10** | 5 | 7 |
| 추가 분석 | 8 | **10** | 1 | 5 |
| 판정 기준 | 9 | **10** | 0 | 7 |
| 실행 편의성 | 9 | 8 | 5 | 7 |
| 코드 완성도 | 9 | **10** | 3 | 7 |
| **총점** | **93** | **94** | **36** | **53** |

### 등급

| 노트북 | 총점 | 등급 | 한 줄 평가 |
|--------|------|------|-----------|
| **2 (Claude 타세션)** | 94 | **A+** | 가장 정교함. DSSP+oligomeric+나이테 검증. 단, C 서열 31aa 오류 |
| **1 (Claude Code)** | 93 | **A** | 서열 정확성 최고. ESMFold 비교표 내장. pTM 추출. 균형 잡힌 설계 |
| **4 (Phase_5c)** | 53 | **D** | 구조는 있지만 서열 오류(C=A) + register 오류 → 실험 무효 |
| **3 (Genspark)** | 36 | **F** | 분석 함수 미완성. salt bridge 과대검출. 판정 코드 없음 |

---

## 7. 각 노트북의 핵심 장단점

### 노트북 1 (Claude Code — 현재 세션): A (93점)
**장점**:
- 서열 3개 모두 확정본과 100% 일치 (유일한 완벽 일치)
- ESMFold Phase 5b-2 결과가 비교 데이터로 내장
- pTM/ipTM 추출 코드 포함
- ColabFold 배치 실행 + 개별 실행 양쪽 지원
- py3Dmol 시각화 (코어=stick, 표면=cartoon)

**단점**:
- DSSP 미사용 (crossing angle에서 비-helix 잔기 포함될 수 있음)
- oligomeric state 판정 없음
- 나이테 순서 검증 (곤<리<건) 없음

### 노트북 2 (Claude 다른 세션): A+ (94점)
**장점**:
- 5개 분석 (salt bridge + core packing + crossing angle + oligomeric + SASA)
- DSSP 기반 crossing angle (가장 정확한 방법)
- scipy cdist 기반 oligomeric state 판정 (TIGHT/WEAK/SEPARATED)
- 나이테 순서 검증 (곤<리<건)
- matplotlib 시각화 (3 패널 비교)
- AMBER + templates 옵션 사용

**단점**:
- Group C 서열이 31aa (2잔기 짧음) — 확정본과 불일치
- ESMFold 비교 데이터 없음
- pTM/ipTM 추출 코드 없음

### 노트북 3 (Genspark): F (36점)
**장점**:
- Python API 직접 호출 (`from colabfold.batch import run`) — 간결
- 기본 구조는 갖추고 있음

**단점 (치명적)**:
- Group C 서열 오류 (31aa)
- Core packing: `cb_distance()` 함수만 있고 실제 분석 코드 없음
- Salt bridge: 모든 원자 쌍 비교 → 심각한 과대검출
- Crossing angle: `fit_axis` 함수만 있고 실제 각도 계산 없음
- 판정 기준/코드 완전 부재
- heptad register 매핑 없음
- SASA, oligomeric state 분석 없음

### 노트북 4 (Phase_5c 불명): D (53점)
**장점**:
- 구조화된 설계 (Setup → Run → Analyze → Validate → Export)
- 5 모델 평균 + 표준편차 계산
- pandas DataFrame 활용
- 상세 검증 기준 (A/B/C 각각)

**단점 (치명적)**:
- **Group C = Group A** (변이 없음) → 실험 자체가 무의미
- 모든 서열 32aa (첫 R 누락)
- Heptad register 1위치 밀림 → a,d 위치 측정 오류
- FASTA 형식 오류 (별도 header 방식)
- 확정 서열과 완전 불일치
- `np.linalg.eig` 사용 (공분산행렬에 부적합)
- 판정 기준은 있지만 기반 데이터가 틀려서 무의미

---

## 8. 통합 제안: 최적 노트북 설계

각 노트북의 장점을 결합한 이상적인 구조:

```
서열: 노트북 1 (Claude Code) → 확정본 33aa 3개
ColabFold: 노트북 2 (Claude) → AMBER + templates + 개별 실행
Salt bridge: 노트북 2 (Claude) → canonical e-g' + regular/irregular 분류
Core packing: 노트북 1/2 공통 → a↔a', d↔d', a↔d' 전체 비교
Crossing angle: 노트북 2 (Claude) → DSSP 기반 helix-only PCA
추가 분석:
  - 노트북 2 → oligomeric state + 나이테 순서
  - 노트북 1 → SASA burial_ratio + pTM/ipTM + ESMFold 비교
시각화:
  - 노트북 1 → py3Dmol 3D 구조
  - 노트북 2 → matplotlib 3패널 비교
판정: 노트북 2의 5개 기준 + 노트북 1의 ESMFold 대조
```

---

## 9. 핵심 교훈

1. **서열 정확성이 최우선**: 4개 노트북 중 확정 서열을 완벽하게 반영한 것은 1개뿐
2. **Heptad register 오류는 전체 분석을 무효화**: 1위치만 밀려도 a,d↔e,g가 뒤바뀜
3. **Group C = Group A 오류는 치명적**: 변이가 없으면 비교 실험 자체가 불가능
4. **AI 교차 검증의 가치**: 사람이 쓴 32aa 서열을 코드가 33aa로 교정한 것처럼, AI간 교차 검증으로 오류 발견 가능
5. **Salt bridge 원자 선택이 중요**: 모든 원자 vs 기능 원자(OE/NZ) → 결과가 완전히 다름
6. **DSSP 활용은 crossing angle 정확도를 높임**: loop/terminal 잔기를 제외하면 노이즈 감소

---

*리뷰 완료: 2026-02-13, Claude Code*
