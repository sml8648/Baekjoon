def solution(n, build_frame):
    def check_pillar(x, y, installed):
        return y == 0 or (x, y - 1, 0) in installed or (x - 1, y, 1) in installed or (x, y, 1) in installed

    def check_beam(x, y, installed):
        return (x, y - 1, 0) in installed or (x + 1, y - 1, 0) in installed or ((x - 1, y, 1) in installed and (x + 1, y, 1) in installed)

    installed = set()

    for frame in build_frame:
        x, y, a, b = frame

        if b == 1:  # 설치
            if a == 0:  # 기둥 설치
                if check_pillar(x, y, installed):
                    installed.add((x, y, 0))
            else:  # 보 설치
                if check_beam(x, y, installed):
                    installed.add((x, y, 1))
        else:  # 삭제
            if (x, y, a) in installed:
                installed.remove((x, y, a))
                if not all(check_pillar(x, y, installed) if a == 0 else check_beam(x, y, installed) for x, y, a in installed):
                    installed.add((x, y, a))

    return sorted(installed, key=lambda x: (x[0], x[1], x[2]))
