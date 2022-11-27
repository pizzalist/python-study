class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickless, knuts로 새로운 WizCoin 객체를 생성한다."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    
    def value(self):
        """이 WizCoin 객체에 포함된 모든 동전의 가치(크넛 단위)"""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
    

    def weightIngrams(self):
        """그램 단위로 동전의 무게를 반환한다."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
    