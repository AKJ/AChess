import board
import chess
import wx

def main ():
	game = chess.Board()
	app = wx.App()
	frame = wx.Frame(None, wx.ID_ANY, "Chess")
	current = board.ChessBoard(frame, wx.ID_ANY, game, 0)
	frame.Show(True)
	app.MainLoop()

if __name__ == "__main__":
	main()
