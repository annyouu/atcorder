import sys
from datetime import datetime, timedelta

def main(lines):
    A = int(lines[0])
    room_info = [line.split() for line in lines[1:A+1]]
    requests = [line.split() for line in lines[A+1:]]

    # 部屋ごとの情報
    room_state = {room[0]: 'empty' for room in room_info}
    room_capacity = {room[0]: int(room[1]) for room in room_info}
    room_price = {room[0]: int(room[2]) for room in room_info}

    room_use = {}        
    checkin_time = {}     
    cleaning_end = {}   

    for val in requests:
        time_str = val[0]
        action = val[1]
        current_time = datetime.fromisoformat(time_str)

        if action == "check-in":
            room_id = val[2]
            adults = int(val[3])
            children = int(val[4])
            days = int(val[5])
            guest_id = val[6]

            # 清掃が完了しているか確認
            if room_id in cleaning_end and current_time >= cleaning_end[room_id]:
                room_state[room_id] = 'empty'
                del cleaning_end[room_id]

            # エラー判定
            if room_state[room_id] == 'occupied':
                print(f"{time_str} check-in error: {room_id} is occupied.")
            elif room_state[room_id] == 'cleaning':
                print(f"{time_str} check-in error: {room_id} is being cleaned.")
            elif adults + children > room_capacity[room_id]:
                print(f"{time_str} check-in error: {room_id} cannot accommodate {guest_id}.")
            else:
                print(f"{time_str} check-in {guest_id} successfully checked in to {room_id}.")
                room_state[room_id] = 'occupied'
                room_use[guest_id] = room_id
                checkin_time[guest_id] = (current_time, days, adults, children)

        elif action == "check-out":
            guest_id = val[2]
            room_id = val[3]
            cleaning_duration = int(val[4])

            if guest_id not in room_use:
                print(f"{time_str} check-out error: {guest_id} does not exist.")
            elif room_use[guest_id] != room_id:
                print(f"{time_str} check-out error: {guest_id} is not in {room_id}.")
            else:
                start_time, days, adults, children = checkin_time[guest_id]
                one_day_charge = room_price[room_id] * adults + int(room_price[room_id] * 0.8) * children
                total_charge = one_day_charge * days
                print(f"{time_str} check-out {guest_id} has to pay {total_charge} to leave {room_id}.")

                # 清掃処理
                room_state[room_id] = 'cleaning'
                clean_end_time = current_time + timedelta(minutes=cleaning_duration)
                print(f"cleaning of {room_id} will be completed at {clean_end_time.isoformat()}.")
                cleaning_end[room_id] = clean_end_time

                # 宿泊客データ削除
                del room_use[guest_id]
                del checkin_time[guest_id]

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in sys.stdin]
    main(lines)

