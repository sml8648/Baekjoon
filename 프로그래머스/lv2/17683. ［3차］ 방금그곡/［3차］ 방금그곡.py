from datetime import timedelta
def str_replace(str):

    str = str.replace('A#','1')
    str = str.replace('C#','2')
    str = str.replace('D#','3')
    str = str.replace('F#','4')
    str = str.replace('G#','5')

    return str

def solution(m, musicinfos):

    new_m = str_replace(m)

    result = []
    for idx, each in enumerate(musicinfos):

        tmp = each.split(',')
        
        start = tmp[0].split(':')
        end = tmp[1].split(':')
        
        start_time = timedelta(hours = int(start[0]), minutes = int(start[1]))
        end_time = timedelta(hours = int(end[0]), minutes = int(end[1]))

        time_diff = ((end_time - start_time).seconds) // 60
        new_song = str_replace(tmp[3])

        div, remain = divmod(time_diff, len(new_song))

        new_song = new_song*div + new_song[:remain]

        if new_m in new_song:

            tmp_result = (idx, time_diff, tmp[2])
            result.append(tmp_result)

    if not len(result):
        return "(None)"
    else:
        result.sort(key=lambda x: (-x[1],x[0]))

        return result[0][2]