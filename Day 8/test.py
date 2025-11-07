


class BankingSystemImpl():

    def __init__(self):
        # TODO: implement
        self.acc_ids = {}
        self.top_spender = {}

    # TODO: implement interface methods here
    def create_account(self,timestamp,account_id):
        self.timestamp = timestamp
        if account_id in self.acc_ids.keys():
            return False
        self.acc_ids[account_id] = 0
        self.top_spender[account_id] = 0
        return True
        
        
        
    def deposit(self,timestamp,account_id,amount):
        if account_id not in self.acc_ids.keys():
            return None
        self.acc_ids[account_id] += amount
        return self.acc_ids[account_id]
    def transfer(self,timestamp,source_account_id,target_account_id,amount):
        if source_account_id == target_account_id or source_account_id not in self.acc_ids.keys() or target_account_id not in self.acc_ids.keys():
            return None
        if self.acc_ids[source_account_id] < amount:
            return None
        self.acc_ids[source_account_id] -= amount
        self.top_spender[source_account_id] += amount 
        self.acc_ids[target_account_id] += amount 
        return self.acc_ids[source_account_id]
        
    def top_spenders(self,timestamp,n):
        print(self.top_spender.items())
        sorted_dict =  sorted(self.top_spender.items(),key=lambda x: x[1],reverse=True)
        ans = []
        for item in sorted_dict:
            ans.append(f"{item[0]}({item[1]})")
        print(type(ans))
        return ans

system = BankingSystemImpl()
system.create_account(1, 'account1')
system.create_account(2, 'account2')
system.create_account(3, 'account3')
system.deposit(4, 'account1', 1000)
system.deposit(5, 'account2', 1000)
system.deposit(6, 'account3', 1000)
system.transfer(7, 'account2', 'account3', 100)
system.transfer(8, 'account2', 'account3', 100)
system.transfer(9, 'account3', 'account1', 100)
expected = ['account2(200)', 'account3(100)', 'account1(0)']
print(system.top_spender.items())
print(system.top_spenders(10, 3))
            
        
