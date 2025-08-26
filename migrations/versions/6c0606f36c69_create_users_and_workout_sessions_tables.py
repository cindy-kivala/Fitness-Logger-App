"""create users and workout_sessions tables

Revision ID: 6c0606f36c69
Revises: f049fe82f1da
Create Date: 2025-08-26 22:53:08.594781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c0606f36c69'
down_revision: Union[str, None] = 'f049fe82f1da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('age', sa.Integer),
        sa.Column('weight', sa.Float)
    )

    op.create_table(
        'workout_sessions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('duration', sa.Integer)  # duration in minutes
    )


def downgrade() -> None:
    op.drop_table('workout_sessions')
    op.drop_table('users')
