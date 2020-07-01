def plot_hist(path):
	hist = pd.read_csv(path)
	acc = hist["accuracy"]
	val_acc = hist["val_accuracy"]

	loss = hist["loss"]
	val_loss = hist["val_loss"] 
	epochs_range = range(len(hist))

	plt.figure(figsize=(8, 8))
	plt.subplot(1, 2, 1)
	plt.plot(epochs_range, acc, label='Training Accuracy')
	plt.plot(epochs_range, val_acc, label='Validation Accuracy')
	plt.legend(loc='lower right')
	plt.title('Training and Validation Accuracy')

	plt.subplot(1, 2, 2)
	plt.plot(epochs_range, loss, label='Training Loss')
	plt.plot(epochs_range, val_loss, label='Validation Loss')
	plt.legend(loc='upper right')
	plt.title('Training and Validation Loss')
	plt.show()