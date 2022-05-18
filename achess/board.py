import chess
import wx

import game
import output

class ChessBoard(wx.Panel):
	def __init__(self, parent, id, *args, **kwargs):
		super(ChessBoard, self).__init__(parent, id, *args, **kwargs)
		self.game = game.ChessGame()
		self.board = game.createBoard()
		self.colors = ["Black", "White"]
		self.marked = None

	def announceMove(self, start, end):
		capturestring = ""
		movestring = "Moved {} {} from {} to {}".format(self.colors[start["color"]], start["piece"], start["name"], end["name"])
		if end["piece"]:
			capturestring = "Captured {}".format(end["piece"])
		output.say("{}. {}".format(movestring, capturestring))

	def announceOutcome(self, board):
		if board.is_checkmate():
			output.say("Checkmate. {} wins!".format(self.colors[board.outcome().winner]))
		elif board.is_check():
			output.say("Check.")
		else:
			return

	def announceSquare(self, loc):
		square = self.game.getSquareData(self.board, loc)
		if not square.piece:
			msg = f"{square.name}"
		else:
			msg = f"{square.name} {square.color} {square.piece}"
		output.say(msg)

	def mark(self, board, loc):
		square = game.getSquareData(self.board, loc)
		if not self.marked:
			if not square["piece"] or self.board.turn != square["color"]:
				return
			else:
				self.marked = loc
				output.say("{} marked.".format(square["piece"]))
		elif self.marked and self.marked == loc:
			self.marked = None
			output.say("{} unmarked.".format(square["piece"]))
		elif self.marked and self.marked != loc:
			self.handle_move(self.board, self.marked, loc)

	def handle_move(self, board, start, end, promotion=None):
		move, start, end, promoted = game.validateMove(board, start, end, promotion)
		if move:
			board.push(move)
			self.marked = None
			self.announceMove(self, start, end)
			self.announceOutcome(self, board)
		else:
			output.say("Unexpected error.")

	def navigateBoard(self, board, direction, by="rank"):
		focus = board.focus
		if direction == "plus":
			if by == "rank":
				result = focus + 1
			elif by  == "file":
				result = focus + 8
		elif direction == "minus":
			if by == "rank":
				result = focus - 1
			elif by == "file":
				result = focus - 8
		if result not in chess.SQUARES:
			self.announceSquare(focus)
			return
		focus = result
		self.announceSquare(result)
