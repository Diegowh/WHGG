"""Change LeagueEntry.account_id str to int

Revision ID: 03b883fd3cc6
Revises: 5d64355ddbee
Create Date: 2024-08-22 13:28:39.156532

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03b883fd3cc6'
down_revision: Union[str, None] = '5d64355ddbee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
