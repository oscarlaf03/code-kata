from FraudDetector import FraudDetector

detector = FraudDetector()

detector.process_all_transactions()
frauds = detector.get_fraudulent_transactions()
print('fraud details:\n', frauds)