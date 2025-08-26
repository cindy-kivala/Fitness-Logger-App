"""create exercises table

Revision ID: f049fe82f1da
Revises: create_exercises_table
Create Date: 2025-08-26 22:48:54.160662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f049fe82f1da'
down_revision: Union[str, None] = 'create_exercises_table'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
