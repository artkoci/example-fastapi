"""add column to post table

Revision ID: f5f51b968cfb
Revises: ea0e21410f57
Create Date: 2023-12-18 21:14:17.408219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5f51b968cfb'
down_revision: Union[str, None] = 'ea0e21410f57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts", 
        sa.Column("content", sa.String(), nullable=False)
        )
    pass


def downgrade() -> None:
    op.drop_column('posts', "content")
    pass
