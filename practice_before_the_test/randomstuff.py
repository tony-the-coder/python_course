# router_id = 100
# while router_id <= 100:
#     if router_id % 8 == 0:
#         print(
#             f"Router {router_id}: Configuration audit passed. No security vulnerabilities found."
#         )
#     else:
#         print(f"Router {router_id}: Security alert - Action required.")
#     router_id += 5


sum = 0
values = [2, 4, 6, 8]
for number in values:
    if sum < 20:
        sum = sum + number
print(sum)
