import QtQuick
import QtQuick.Controls
import Massmaker 1.0

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello Massmaker")
        anchors.centerIn: parent
        font.family: Constants.font.family
    }
}
