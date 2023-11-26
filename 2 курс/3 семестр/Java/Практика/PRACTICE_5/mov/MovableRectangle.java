package mirea.mov;

public class MovableRectangle extends MovablePoint implements Movable {
    MovablePoint topLeft, bottomRight;

    boolean hasCorrectSpeed() {
        return topLeft.xSpeed == bottomRight.xSpeed && topLeft.ySpeed == bottomRight.ySpeed;
    }

    public MovableRectangle(int x1, int y1, int x2, int y2, int xSpeed, int ySpeed) {
        super((x1 + x2) / 2, (y1 + y2) / 2, xSpeed, ySpeed);
        topLeft = new MovablePoint(x1, y1, xSpeed, ySpeed);
        bottomRight = new MovablePoint(x2, y2, xSpeed, ySpeed);
    }

    @Override
    public void moveUp() {
        if (this.hasCorrectSpeed()) {
            y += ySpeed;
            topLeft.y += ySpeed;
            bottomRight.y += ySpeed;
        }
    }

    @Override
    public void moveDown() {
        if (this.hasCorrectSpeed()) {
            y -= ySpeed;
            topLeft.y -= ySpeed;
            bottomRight.y -= ySpeed;
        }
    }

    @Override
    public void moveLeft() {
        if (this.hasCorrectSpeed()) {
            x -= xSpeed;
            topLeft.x -= xSpeed;
            bottomRight.x -= xSpeed;
        }
    }

    @Override
    public void moveRight() {
        if (this.hasCorrectSpeed()) {
            x += xSpeed;
            topLeft.x += xSpeed;
            bottomRight.x += xSpeed;
        }
    }
}