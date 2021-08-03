from PyQt5 import QtCore

class Animation(): 
    @property
    def center(self):
        return self._center

    def animation(self,lb, x_center, y_center, parent):         
        initial_rect = QtCore.QRect(
            x_center,
            y_center,
            171,
            171
        )
        zoom_factor = 1.5
        final_rect = QtCore.QRect(
            x_center,
            y_center,
            int(initial_rect.width() * zoom_factor),
            int(initial_rect.height() * zoom_factor),
        )
        final_rect.moveCenter(initial_rect.center())

        an = QtCore.QPropertyAnimation(lb, b"geometry", parent)
        an.setEasingCurve(QtCore.QEasingCurve.InOutSine)
        an.setStartValue(initial_rect)
        an.setEndValue(final_rect)
        an.setDuration(4000)

        return an