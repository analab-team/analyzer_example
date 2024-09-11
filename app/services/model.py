from models.vault import Vault
from schemas.model_result import ModelResult, Reason


class DumpModel:
    def input_score(self, text: str, vault: Vault) -> ModelResult:
        metric = len(text)

        reasons = list()
        reject_flg = False

        if metric > vault.max_request_size:
            reason = Reason(start=vault.max_request_size, stop=len(text))
            reasons.append(reason)
            reject_flg = True
        model_output = ModelResult(
            metric=metric, reasons=reasons, reject_flg=reject_flg
        )

        return model_output

    def output_score(self, text: str, vault: Vault) -> ModelResult:
        metric = len(text)

        reasons = list()
        reject_flg = False

        if metric > vault.max_output_size:
            reason = Reason(start=vault.max_output_size, stop=len(text))
            reasons.append(reason)
            reject_flg = True
        model_output = ModelResult(
            metric=metric, reasons=reasons, reject_flg=reject_flg
        )

        return model_output
