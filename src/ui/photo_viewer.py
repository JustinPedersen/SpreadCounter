"""
Photo viewer widget for the image displays.
"""

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets


class PhotoViewer(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.pixel_map = None
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(44, 44, 44)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setVerticalStretch(1)
        self.setSizePolicy(size_policy)

    def hasPhoto(self):
        """
        If the current photo viewer has a photo.
        """
        return not self._empty

    def fitInView(self, scale=True):
        """
        Fit the image to the view size

        :param bool scale: To preserve the image scale or not.
        """
        rect = QtCore.QRectF(self._photo.pixmap().rect())

        if not rect.isNull():
            self.setSceneRect(rect)

            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixel_map=None):
        """
        Set the image for the photo viewer.

        :param QPixelMap pixel_map: The pixel map to use.
        """
        self._zoom = 0
        if pixel_map and not pixel_map.isNull():
            self._empty = False
            self.pixel_map = pixel_map
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixel_map)
        else:
            self._empty = True
            self.pixel_map = None
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()

    def wheelEvent(self, event):
        """
        Change the zoom level when the mouse wheel is used.

        :param event: Mouse scroll event.
        """
        if self.hasPhoto():
            if event.delta() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        """
        Toggle the ability to drag on the image.
        """
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def setMinMaxFromImage(self, desired_width=500):
        """
        Helper function to set the min and max height of a widget using its own image.
        :param int desired_width: The end width for the object.
        """
        if self.pixel_map:
            scale_factor = self.pixel_map.height() / desired_width

            if scale_factor != 0:
                # This ensures the image's scale in the UI is always the same.
                self.setMaximumHeight(self.parent().height())
                self.setMaximumWidth(self.parent().width())

                self.setMinimumHeight(self.parent().height() * 0.85)
                self.setMinimumWidth(self.pixel_map.width() / scale_factor)

                self.fitInView()
